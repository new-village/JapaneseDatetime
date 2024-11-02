import re
from datetime import datetime

# List of Japanese eras with their names and starting dates
eras = [
    {'name_en': 'Reiwa', 'name_ja': '令和', 'start_date': datetime(2019, 5, 1)},
    {'name_en': 'Heisei', 'name_ja': '平成', 'start_date': datetime(1989, 1, 8)},
    {'name_en': 'Showa', 'name_ja': '昭和', 'start_date': datetime(1926, 12, 25)},
    {'name_en': 'Taisho', 'name_ja': '大正', 'start_date': datetime(1912, 7, 30)},
    {'name_en': 'Meiji', 'name_ja': '明治', 'start_date': datetime(1868, 9, 8)},
]

class jpdatetime(datetime):
    # Unified custom format codes mapping to their handler functions
    custom_formats = {
        '%G': {'parse': 'parse_full_jp_era', 'format': 'format_full_jp_era'},
        '%g': {'parse': 'parse_abbr_jp_era', 'format': 'format_abbr_jp_era'},
        '%E': {'parse': 'parse_full_en_era', 'format': 'format_full_en_era'},
        '%e': {'parse': 'parse_abbr_en_era', 'format': 'format_abbr_en_era'},
    }

    @classmethod
    def strptime(cls, date_string, format_string):
        # Check if custom era format codes are in the format string
        if any(code in format_string for code in cls.custom_formats):
            # Split the format string into tokens
            tokens = cls._tokenize_format_string(format_string)
            regex_pattern = ''
            for token_type, token_value in tokens:
                if token_type == 'format_code':
                    if token_value in cls.custom_formats:
                        # Get the regex pattern for the custom format code
                        handler_name = cls.custom_formats[token_value]['parse']
                        handler = getattr(cls, f"_get_regex_{handler_name}")
                        regex_pattern += handler()
                    else:
                        # Use the standard datetime regex patterns
                        regex_pattern += cls._escape_regex(token_value)
                else:
                    # Escape literals in the regex pattern
                    regex_pattern += re.escape(token_value)

            # Compile the regex pattern
            match = re.match(regex_pattern, date_string)
            if not match:
                raise ValueError(f"time data '{date_string}' does not match format '{format_string}'")

            # Extract date components from matched groups
            components = match.groupdict()
            year, month, day = cls._extract_date_components(components)
            return cls(year, month, day)
        else:
            # Use standard datetime parsing for formats without custom codes
            dt = datetime.strptime(date_string, format_string)
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    def strftime(self, format_string):
        # Check if custom era format codes are in the format string
        if any(code in format_string for code in self.custom_formats):
            tokens = self._tokenize_format_string(format_string)
            result = ''
            for token_type, token_value in tokens:
                if token_type == 'format_code':
                    if token_value in self.custom_formats:
                        # Call the handler function for the custom format code
                        handler_name = self.custom_formats[token_value]['format']
                        handler = getattr(self, f"_{handler_name}")
                        result += handler()
                    else:
                        # Use standard datetime strftime for other format codes
                        result += super().strftime(token_value)
                else:
                    # Append literals as is
                    result += token_value
            return result
        else:
            # Use standard datetime strftime for formats without custom codes
            return super().strftime(format_string)

    @classmethod
    def _tokenize_format_string(cls, format_string):
        """Tokenizes the format string into format codes and literals."""
        tokens = []
        pattern = re.compile(r'(%.)')
        parts = pattern.split(format_string)
        for part in parts:
            if part.startswith('%') and len(part) > 1:
                tokens.append(('format_code', part))
            else:
                tokens.append(('literal', part))
        return tokens

    @staticmethod
    def _escape_regex(format_code):
        """Escapes standard format codes for regex."""
        regex_patterns = {
            '%Y': r'(?P<year>\d{4})',
            '%m': r'(?P<month>\d{1,2})',
            '%d': r'(?P<day>\d{1,2})',
            '%B': r'(?P<month_name>[A-Za-z]+)',
            # Add other standard patterns as needed
        }
        return regex_patterns.get(format_code, re.escape(format_code))

    @classmethod
    def _get_regex_parse_full_jp_era(cls):
        """Returns the regex pattern for full Japanese era names."""
        era_names = '|'.join([era['name_ja'] for era in eras])
        return rf'(?P<era_full_jp>{era_names})(?P<era_year>元|\d+)'

    @classmethod
    def _get_regex_parse_abbr_jp_era(cls):
        """Returns the regex pattern for abbreviated Japanese era names."""
        era_abbrs = ''.join([era['name_ja'][0] for era in eras])
        return rf'(?P<era_abbr_jp>[{era_abbrs}])(?P<era_year>元|\d+)'

    @classmethod
    def _get_regex_parse_full_en_era(cls):
        """Returns the regex pattern for full English era names."""
        era_names = '|'.join([era['name_en'] for era in eras])
        return rf'(?P<era_full_en>{era_names}) (?P<era_year>First|\d+)'

    @classmethod
    def _get_regex_parse_abbr_en_era(cls):
        """Returns the regex pattern for abbreviated English era names."""
        era_abbrs = ''.join([era['name_en'][0] for era in eras])
        return rf'(?P<era_abbr_en>[{era_abbrs}])(?P<era_year>First|\d+)'

    @classmethod
    def _extract_date_components(cls, components):
        """Extracts and calculates the date components from regex match groups."""
        # Initialize default values
        year = month = day = None

        # Handle era information
        era = None
        era_year_str = components.get('era_year')
        if 'era_full_jp' in components and components['era_full_jp']:
            era_name = components['era_full_jp']
            era = next((e for e in eras if e['name_ja'] == era_name), None)
        elif 'era_abbr_jp' in components and components['era_abbr_jp']:
            era_abbr = components['era_abbr_jp']
            era = next((e for e in eras if e['name_ja'][0] == era_abbr), None)
        elif 'era_full_en' in components and components['era_full_en']:
            era_name = components['era_full_en']
            era = next((e for e in eras if e['name_en'] == era_name), None)
        elif 'era_abbr_en' in components and components['era_abbr_en']:
            era_abbr = components['era_abbr_en']
            era = next((e for e in eras if e['name_en'][0] == era_abbr), None)

        # Determine the era year
        if era and era_year_str:
            if era_year_str in ('元', 'First'):
                era_year = 1
            else:
                era_year = int(era_year_str)
            year = era['start_date'].year + era_year - 1

        # Handle standard year if era is not used
        if not year and 'year' in components:
            year = int(components['year'])

        # Handle month
        if 'month' in components and components['month']:
            month = int(components['month'])
        elif 'month_name' in components and components['month_name']:
            month_name = components['month_name']
            month = datetime.strptime(month_name, '%B').month

        # Handle day
        if 'day' in components and components['day']:
            day = int(components['day'])

        if None in (year, month, day):
            raise ValueError("Incomplete date information")

        return year, month, day

    def _get_era_info(self):
        """Retrieves the era information for the current date."""
        for era in eras:
            if self >= era['start_date']:
                return era
        raise ValueError("Date out of range for Japanese eras")

    def _format_full_jp_era(self):
        """Formats the date using full Japanese era name."""
        era = self._get_era_info()
        era_year = self.year - era['start_date'].year + 1
        era_year_str = '元' if era_year == 1 else str(era_year)
        return f"{era['name_ja']}{era_year_str}"

    def _format_abbr_jp_era(self):
        """Formats the date using abbreviated Japanese era name."""
        era = self._get_era_info()
        era_year = self.year - era['start_date'].year + 1
        era_abbr = era['name_ja'][0]
        era_year_str = str(era_year)
        return f"{era_abbr}{era_year_str}"

    def _format_full_en_era(self):
        """Formats the date using full English era name."""
        era = self._get_era_info()
        era_year = self.year - era['start_date'].year + 1
        era_year_str = str(era_year)
        return f"{era['name_en']} {era_year_str}"

    def _format_abbr_en_era(self):
        """Formats the date using abbreviated English era name."""
        era = self._get_era_info()
        era_year = self.year - era['start_date'].year + 1
        era_abbr = era['name_en'][0]
        era_year_str = str(era_year)
        return f"{era_abbr}{era_year_str}"
