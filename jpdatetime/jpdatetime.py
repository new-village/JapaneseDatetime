from datetime import datetime

class jpdatetime(datetime):
    ERA_MAP = [
        ("令和", datetime(2019, 5, 1)),
        ("平成", datetime(1989, 1, 8)),
        ("昭和", datetime(1926, 12, 25)),
        ("大正", datetime(1912, 7, 30)),
        ("明治", datetime(1868, 1, 25))
    ]

    @classmethod
    def strptime(cls, date_string, format_string):
        for era_name, start_year in cls.ERA_MAP:
            if era_name in date_string:
                date_string_wo_era = date_string.replace(era_name, "").strip()
                year_in_era = int(date_string_wo_era.split("年")[0].strip())
                western_year = start_year.year + year_in_era - 1
                date_string_wo_era = date_string_wo_era.replace(str(year_in_era), str(western_year), 1)
                date_string = f"{western_year}年{date_string_wo_era.split('年', 1)[1]}"
                format_string = format_string.replace("%j", "%Y")
                return super().strptime(date_string, format_string)
        return super().strptime(date_string, format_string)

    def strftime(self, format_string):
        if "%j" in format_string:
            era, year_in_era = self.get_japanese_era()
            if era:
                format_string = format_string.replace("%j", f"{era}{year_in_era}")
        return super().strftime(format_string)

    def get_japanese_era(self):
        for era, start_date in jpdatetime.ERA_MAP:
            if self >= start_date:
                year_in_era = self.year - start_date.year + 1
                return era, year_in_era
        return "", self.year

