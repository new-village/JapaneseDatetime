import unittest
from datetime import datetime
from JapaneseDatetime import JapaneseDatetime

class TestJapaneseDatetime(unittest.TestCase):
    def setUp(self):
        self.test_cases_strptime = [
            ("令和5年10月30日", "%j年%m月%d日", JapaneseDatetime(2023, 10, 30)),
            ("平成30年4月1日", "%j年%m月%d日", JapaneseDatetime(2018, 4, 1)),
            ("昭和64年1月7日", "%j年%m月%d日", JapaneseDatetime(1989, 1, 7)),
            ("大正15年12月24日", "%j年%m月%d日", JapaneseDatetime(1926, 12, 24)),
            ("明治45年7月29日", "%j年%m月%d日", JapaneseDatetime(1912, 7, 29))
        ]

        self.test_cases_strftime = [
            (JapaneseDatetime(2024, 10, 30), "%j年%m月%d日", "令和6年10月30日"),
            (JapaneseDatetime(2018, 4, 1), "%j年%m月%d日", "平成30年04月01日"),
            (JapaneseDatetime(1989, 1, 7), "%j年%m月%d日", "昭和64年01月07日"),
            (JapaneseDatetime(1926, 12, 24), "%j年%m月%d日", "大正15年12月24日"),
            (JapaneseDatetime(1912, 7, 29), "%j年%m月%d日", "明治45年07月29日")
        ]

    def test_strptime(self):
        for date_string, format_string, expected_date in self.test_cases_strptime:
            with self.subTest(date_string=date_string):
                self.assertEqual(JapaneseDatetime.strptime(date_string, format_string), expected_date)

    def test_strftime(self):
        for date, format_string, expected_output in self.test_cases_strftime:
            with self.subTest(date=date):
                self.assertEqual(date.strftime(format_string), expected_output)

if __name__ == "__main__":
    unittest.main()
