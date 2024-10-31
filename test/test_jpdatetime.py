import unittest
from datetime import datetime
from jpdatetime import jpdatetime

class Testjpdatetime(unittest.TestCase):
    def setUp(self):
        self.test_cases_strptime = [
            ("令和5年10月30日", "%j年%m月%d日", jpdatetime(2023, 10, 30)),
            ("平成30年4月1日", "%j年%m月%d日", jpdatetime(2018, 4, 1)),
            ("昭和64年1月7日", "%j年%m月%d日", jpdatetime(1989, 1, 7)),
            ("大正15年12月24日", "%j年%m月%d日", jpdatetime(1926, 12, 24)),
            ("明治45年7月29日", "%j年%m月%d日", jpdatetime(1912, 7, 29)),
            ("令和1年5月1日", "%j年%m月%d日", jpdatetime(2019, 5, 1)),
            ("平成1年1月8日", "%j年%m月%d日", jpdatetime(1989, 1, 8)),
            ("令和元年5月1日", "%j年%m月%d日", jpdatetime(2019, 5, 1)),
            ("平成元年1月8日", "%j年%m月%d日", jpdatetime(1989, 1, 8))
        ]

        self.test_cases_strftime = [
            (jpdatetime(2024, 10, 30), "%j年%m月%d日", "令和6年10月30日"),
            (jpdatetime(2018, 4, 1), "%j年%m月%d日", "平成30年04月01日"),
            (jpdatetime(1989, 1, 7), "%j年%m月%d日", "昭和64年01月07日"),
            (jpdatetime(1926, 12, 24), "%j年%m月%d日", "大正15年12月24日"),
            (jpdatetime(1912, 7, 29), "%j年%m月%d日", "明治45年07月29日"),
            (jpdatetime(2019, 5, 1), "%j年%m月%d日", "令和元年05月01日"),
            (jpdatetime(1989, 1, 8), "%j年%m月%d日", "平成元年01月08日")
        ]

    def test_strptime(self):
        for date_string, format_string, expected_date in self.test_cases_strptime:
            with self.subTest(date_string=date_string):
                self.assertEqual(jpdatetime.strptime(date_string, format_string), expected_date)

    def test_strftime(self):
        for date, format_string, expected_output in self.test_cases_strftime:
            with self.subTest(date=date):
                self.assertEqual(date.strftime(format_string), expected_output)

if __name__ == "__main__":
    unittest.main()
