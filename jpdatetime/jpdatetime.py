from datetime import datetime

class jpdatetime(datetime):
    # Mapping of Japanese eras to their starting dates and short names
    ERA_MAP = {
        "令和": {"short": "令", "start_date": datetime(2019, 5, 1)},
        "平成": {"short": "平", "start_date": datetime(1989, 1, 8)},
        "昭和": {"short": "昭", "start_date": datetime(1926, 12, 25)},
        "大正": {"short": "大", "start_date": datetime(1912, 7, 30)},
        "明治": {"short": "明", "start_date": datetime(1868, 9, 8)}
    }

    @classmethod
    def strptime(cls, date_string, format_string):
        """
        Parse a string representing a date in Japanese era format to a jpdatetime object.

        Args:
            date_string (str): The date string in Japanese era format.
            format_string (str): The format string, where %G is used to represent the era.

        Returns:
            jpdatetime: Parsed jpdatetime object.
        """
        era_name, year_in_era, date_string_wo_era = cls._extract_era_info(date_string)
        if era_name:
            start_year = cls._get_start_year(era_name)
            western_year = start_year + year_in_era - 1
            date_string = f"{western_year}年{date_string_wo_era}"
            format_string = format_string.replace("%G", "%Y").replace("%g", "%Y")
        return super().strptime(date_string, format_string)

    @classmethod
    def _extract_era_info(cls, date_string):
        """
        Extract the era name and year from the date string.

        Args:
            date_string (str): The date string in Japanese era format.

        Returns:
            tuple: A tuple containing the era name, year in the era, and remaining date string.
        """
        for era_name, era_info in cls.ERA_MAP.items():
            short_name = era_info["short"]
            if era_name in date_string:
                date_string_wo_era = date_string.replace(era_name, "").strip()
                year_part = date_string_wo_era.split("年")[0].strip()
                year_in_era = 1 if year_part == "元" else int(year_part)
                date_string_wo_era = date_string_wo_era.split("年", 1)[1]
                return era_name, year_in_era, date_string_wo_era
            elif short_name in date_string:
                date_string_wo_era = date_string.replace(short_name, "").strip()
                year_part = date_string_wo_era.split("年")[0].strip()
                year_in_era = 1 if year_part == "元" else int(year_part)
                date_string_wo_era = date_string_wo_era.split("年", 1)[1]
                return era_name, year_in_era, date_string_wo_era
        return None, None, None

    @classmethod
    def _get_start_year(cls, era_name):
        """
        Get the starting year of the specified era.

        Args:
            era_name (str): The name of the Japanese era.

        Returns:
            int: The starting year of the era.

        Raises:
            ValueError: If the era name is unknown.
        """
        if era_name in cls.ERA_MAP:
            return cls.ERA_MAP[era_name]["start_date"].year
        raise ValueError(f"Unknown era: {era_name}")

    def strftime(self, format_string):
        """
        Format the date using a given format string, supporting Japanese era notation.

        Args:
            format_string (str): The format string, where %G represents the Japanese era.

        Returns:
            str: Formatted date string.
        """
        if "%G" in format_string or "%g" in format_string:
            era, year_in_era = self._get_japanese_era()
            if era:
                year_display = "元" if year_in_era == 1 else str(year_in_era)
                short_era = self.ERA_MAP[era]["short"]
                if "%G" in format_string:
                    format_string = format_string.replace("%G", f"{era}{year_display}")
                if "%g" in format_string:
                    format_string = format_string.replace("%g", f"{short_era}{year_display}")
        return super().strftime(format_string)

    def _get_japanese_era(self):
        """
        Determine the Japanese era and the year within that era for the current date.

        Returns:
            tuple: A tuple containing the era name and the year within the era.
        """
        for era, era_info in jpdatetime.ERA_MAP.items():
            start_date = era_info["start_date"]
            if self >= start_date:
                year_in_era = self.year - start_date.year + 1
                return era, year_in_era
        return "", self.year
