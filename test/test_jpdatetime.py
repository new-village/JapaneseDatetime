import unittest
from datetime import datetime
from jpdatetime import jpdatetime

class Testjpdatetime(unittest.TestCase):
    def setUp(self):
        # Test cases for %G format (Full Japanese Era Name)
        self.test_cases_strptime_G = [
            # Existing test cases
            ("令和5年10月30日", "%G年%m月%d日", datetime(2023, 10, 30)),
            ("平成30年4月1日", "%G年%m月%d日", datetime(2018, 4, 1)),
            ("昭和64年1月7日", "%G年%m月%d日", datetime(1989, 1, 7)),
            ("大正15年12月24日", "%G年%m月%d日", datetime(1926, 12, 24)),
            ("明治45年7月29日", "%G年%m月%d日", datetime(1912, 7, 29)),
            ("令和元年5月1日", "%G年%m月%d日", datetime(2019, 5, 1)),
            ("平成元年1月8日", "%G年%m月%d日", datetime(1989, 1, 8)),
            # Additional test cases
            ("令和6年1月1日", "%G年%m月%d日", datetime(2024, 1, 1)),
            ("平成元年12月31日", "%G年%m月%d日", datetime(1989, 12, 31)),
            ("昭和元年12月25日", "%G年%m月%d日", datetime(1926, 12, 25)),
            ("大正元年7月30日", "%G年%m月%d日", datetime(1912, 7, 30)),
            ("明治元年9月8日", "%G年%m月%d日", datetime(1868, 9, 8)),
            # Edge case: Date just before an era change
            ("平成31年4月30日", "%G年%m月%d日", datetime(2019, 4, 30)),
            # Edge case: Era start date
            ("令和元年5月1日", "%G年%m月%d日", datetime(2019, 5, 1)),
            # Leap year
            ("平成4年2月29日", "%G年%m月%d日", datetime(1992, 2, 29)),
        ]

        # Test cases for %g format (Abbreviated Japanese Era Name)
        self.test_cases_strptime_g = [
            # Existing test cases
            ("令5年10月30日", "%g年%m月%d日", datetime(2023, 10, 30)),
            ("平30年4月1日", "%g年%m月%d日", datetime(2018, 4, 1)),
            ("昭64年1月7日", "%g年%m月%d日", datetime(1989, 1, 7)),
            ("大1年7月30日", "%g年%m月%d日", datetime(1912, 7, 30)),
            ("明45年7月29日", "%g年%m月%d日", datetime(1912, 7, 29)),
            # Additional test cases
            ("令1年5月1日", "%g年%m月%d日", datetime(2019, 5, 1)),
            ("平1年1月8日", "%g年%m月%d日", datetime(1989, 1, 8)),
            ("昭1年12月25日", "%g年%m月%d日", datetime(1926, 12, 25)),
            ("大元年7月30日", "%g年%m月%d日", datetime(1912, 7, 30)),
            ("明元年9月8日", "%g年%m月%d日", datetime(1868, 9, 8)),
            # Edge case: Date just before an era change
            ("平31年4月30日", "%g年%m月%d日", datetime(2019, 4, 30)),
            # Leap year
            ("平4年2月29日", "%g年%m月%d日", datetime(1992, 2, 29)),
        ]

        # Test cases for %E format (Full English Era Name)
        self.test_cases_strptime_E = [
            # Existing test cases
            ("Reiwa 5, October 30", "%E, %B %d", datetime(2023, 10, 30)),
            ("Heisei 30, April 1", "%E, %B %d", datetime(2018, 4, 1)),
            ("Showa 64, January 7", "%E, %B %d", datetime(1989, 1, 7)),
            ("Taisho 15, December 24", "%E, %B %d", datetime(1926, 12, 24)),
            ("Meiji 45, July 29", "%E, %B %d", datetime(1912, 7, 29)),
            # Additional test cases
            ("Reiwa 1, May 1", "%E, %B %d", datetime(2019, 5, 1)),
            ("Heisei 1, January 8", "%E, %B %d", datetime(1989, 1, 8)),
            ("Showa 1, December 25", "%E, %B %d", datetime(1926, 12, 25)),
            ("Taisho 1, July 30", "%E, %B %d", datetime(1912, 7, 30)),
            ("Meiji 1, September 8", "%E, %B %d", datetime(1868, 9, 8)),
            # Edge case: Date just before an era change
            ("Heisei 31, April 30", "%E, %B %d", datetime(2019, 4, 30)),
            # Leap year
            ("Heisei 4, February 29", "%E, %B %d", datetime(1992, 2, 29)),
        ]

        # Test cases for %e format (Abbreviated English Era Name)
        self.test_cases_strptime_e = [
            # Existing test cases
            ("R5/10/30", "%e/%m/%d", datetime(2023, 10, 30)),
            ("H30/4/1", "%e/%m/%d", datetime(2018, 4, 1)),
            ("S64/1/7", "%e/%m/%d", datetime(1989, 1, 7)),
            ("T15/12/24", "%e/%m/%d", datetime(1926, 12, 24)),
            ("M45/7/29", "%e/%m/%d", datetime(1912, 7, 29)),
            # Additional test cases
            ("R1/5/1", "%e/%m/%d", datetime(2019, 5, 1)),
            ("H1/1/8", "%e/%m/%d", datetime(1989, 1, 8)),
            ("S1/12/25", "%e/%m/%d", datetime(1926, 12, 25)),
            ("T1/7/30", "%e/%m/%d", datetime(1912, 7, 30)),
            ("M1/9/8", "%e/%m/%d", datetime(1868, 9, 8)),
            # Edge case: Date just before an era change
            ("H31/4/30", "%e/%m/%d", datetime(2019, 4, 30)),
            # Leap year
            ("H4/02/29", "%e/%m/%d", datetime(1992, 2, 29)),
        ]

        # Separate test cases for strftime (%G)
        self.test_cases_strftime_G = [
            # Existing test cases
            (jpdatetime(2024, 10, 30), "%G年%m月%d日", "令和6年10月30日"),
            (jpdatetime(2018, 4, 1), "%G年%m月%d日", "平成30年04月01日"),
            (jpdatetime(1989, 1, 7), "%G年%m月%d日", "昭和64年01月07日"),
            (jpdatetime(1926, 12, 24), "%G年%m月%d日", "大正15年12月24日"),
            (jpdatetime(1912, 7, 29), "%G年%m月%d日", "明治45年07月29日"),
            (jpdatetime(2019, 5, 1), "%G年%m月%d日", "令和元年05月01日"),
            (jpdatetime(1989, 1, 8), "%G年%m月%d日", "平成元年01月08日"),
            # Additional test cases
            (jpdatetime(1926, 12, 25), "%G年%m月%d日", "昭和元年12月25日"),
            (jpdatetime(1912, 7, 30), "%G年%m月%d日", "大正元年07月30日"),
            (jpdatetime(1868, 9, 8), "%G年%m月%d日", "明治元年09月08日"),
            # Edge case: Date just before an era change
            (jpdatetime(2019, 4, 30), "%G年%m月%d日", "平成31年04月30日"),
            # Leap year
            (jpdatetime(1992, 2, 29), "%G年%m月%d日", "平成4年02月29日"),
        ]

        # Separate test cases for strftime (%g)
        self.test_cases_strftime_g = [
            # Existing test cases
            (jpdatetime(2023, 10, 30), "%g年%m月%d日", "令5年10月30日"),
            (jpdatetime(2018, 4, 1), "%g年%m月%d日", "平30年04月01日"),
            (jpdatetime(1989, 1, 7), "%g年%m月%d日", "昭64年01月07日"),
            (jpdatetime(1912, 7, 30), "%g年%m月%d日", "大1年07月30日"),
            (jpdatetime(1912, 7, 29), "%g年%m月%d日", "明45年07月29日"),
            # Additional test cases
            (jpdatetime(2019, 5, 1), "%g年%m月%d日", "令1年05月01日"),
            (jpdatetime(1989, 1, 8), "%g年%m月%d日", "平1年01月08日"),
            (jpdatetime(1926, 12, 25), "%g年%m月%d日", "昭1年12月25日"),
            (jpdatetime(1868, 9, 8), "%g年%m月%d日", "明1年09月08日"),
            # Edge case: Date just before an era change
            (jpdatetime(2019, 4, 30), "%g年%m月%d日", "平31年04月30日"),
            # Leap year
            (jpdatetime(1992, 2, 29), "%g年%m月%d日", "平4年02月29日"),
        ]

        # Separate test cases for strftime (%E)
        self.test_cases_strftime_E = [
            # Existing test cases
            (jpdatetime(2023, 10, 30), "%E, %B %d", "Reiwa 5, October 30"),
            (jpdatetime(2018, 4, 1), "%E, %B %d", "Heisei 30, April 01"),
            (jpdatetime(1989, 1, 7), "%E, %B %d", "Showa 64, January 07"),
            (jpdatetime(1912, 7, 30), "%E, %B %d", "Taisho 1, July 30"),
            (jpdatetime(1912, 7, 29), "%E, %B %d", "Meiji 45, July 29"),
            # Additional test cases
            (jpdatetime(2019, 5, 1), "%E, %B %d", "Reiwa 1, May 01"),
            (jpdatetime(1989, 1, 8), "%E, %B %d", "Heisei 1, January 08"),
            (jpdatetime(1926, 12, 25), "%E, %B %d", "Showa 1, December 25"),
            (jpdatetime(1868, 9, 8), "%E, %B %d", "Meiji 1, September 08"),
            # Edge case: Date just before an era change
            (jpdatetime(2019, 4, 30), "%E, %B %d", "Heisei 31, April 30"),
            # Leap year
            (jpdatetime(1992, 2, 29), "%E, %B %d", "Heisei 4, February 29"),
        ]

        # Separate test cases for strftime (%e)
        self.test_cases_strftime_e = [
            # Existing test cases
            (jpdatetime(2023, 10, 30), "%e/%m/%d", "R5/10/30"),
            (jpdatetime(2018, 4, 1), "%e/%m/%d", "H30/04/01"),
            (jpdatetime(1989, 1, 7), "%e/%m/%d", "S64/01/07"),
            (jpdatetime(1912, 7, 30), "%e/%m/%d", "T1/07/30"),
            (jpdatetime(1912, 7, 29), "%e/%m/%d", "M45/07/29"),
            # Additional test cases
            (jpdatetime(2019, 5, 1), "%e/%m/%d", "R1/05/01"),
            (jpdatetime(1989, 1, 8), "%e/%m/%d", "H1/01/08"),
            (jpdatetime(1926, 12, 25), "%e/%m/%d", "S1/12/25"),
            (jpdatetime(1868, 9, 8), "%e/%m/%d", "M1/09/08"),
            # Edge case: Date just before an era change
            (jpdatetime(2019, 4, 30), "%e/%m/%d", "H31/04/30"),
            # Leap year
            (jpdatetime(1992, 2, 29), "%e/%m/%d", "H4/02/29"),
        ]

    def test_strptime_full_jpEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_G:
            with self.subTest(date_string=date_string):
                self.assertEqual(jpdatetime.strptime(date_string, format_string), expected_date)

    def test_strptime_abbr_jpEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_g:
            with self.subTest(date_string=date_string):
                self.assertEqual(jpdatetime.strptime(date_string, format_string), expected_date)

    def test_strptime_full_enEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_E:
            with self.subTest(date_string=date_string):
                self.assertEqual(jpdatetime.strptime(date_string, format_string), expected_date)

    def test_strptime_abbr_enEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_e:
            with self.subTest(date_string=date_string):
                self.assertEqual(jpdatetime.strptime(date_string, format_string), expected_date)

    def test_strftime_full_jpEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_G:
            with self.subTest(date=date):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strftime_abbr_jpEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_g:
            with self.subTest(date=date):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strftime_full_enEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_E:
            with self.subTest(date=date):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strftime_abbr_enEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_e:
            with self.subTest(date=date):
                self.assertEqual(date.strftime(format_string), expected_output)

if __name__ == "__main__":
    unittest.main()
