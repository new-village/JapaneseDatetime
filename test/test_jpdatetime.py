import unittest
from datetime import datetime
from jpdatetime import jpdatetime

class Testjpdatetime(unittest.TestCase):
    def setUp(self):
        # Test cases for strftime with %G format (Full Japanese Era Name)
        self.test_cases_strftime_G = [
            # Reiwa Era
            (jpdatetime(2023, 10, 30), "%G年%m月%d日", "令和05年10月30日"),
            (jpdatetime(2023, 10, 30), "%-G年%m月%d日", "令和5年10月30日"),
            (jpdatetime(2019, 5, 1), "%G年%m月%d日", "令和元年05月01日"),
            (jpdatetime(2019, 5, 1), "%-G年%m月%d日", "令和元年05月01日"),
            # Heisei Era
            (jpdatetime(2018, 4, 1), "%G年%m月%d日", "平成30年04月01日"),
            (jpdatetime(2018, 4, 1), "%-G年%m月%d日", "平成30年04月01日"),
            (jpdatetime(1989, 1, 8), "%G年%m月%d日", "平成元年01月08日"),
            (jpdatetime(1989, 1, 8), "%-G年%m月%d日", "平成元年01月08日"),
            # Showa Era
            (jpdatetime(1989, 1, 7), "%G年%m月%d日", "昭和64年01月07日"),
            (jpdatetime(1989, 1, 7), "%-G年%m月%d日", "昭和64年01月07日"),
            (jpdatetime(1926, 12, 25), "%G年%m月%d日", "昭和元年12月25日"),
            (jpdatetime(1926, 12, 25), "%-G年%m月%d日", "昭和元年12月25日"),
            # Taisho Era
            (jpdatetime(1926, 12, 24), "%G年%m月%d日", "大正15年12月24日"),
            (jpdatetime(1926, 12, 24), "%-G年%m月%d日", "大正15年12月24日"),
            (jpdatetime(1912, 7, 30), "%G年%m月%d日", "大正元年07月30日"),
            (jpdatetime(1912, 7, 30), "%-G年%m月%d日", "大正元年07月30日"),
            # Meiji Era
            (jpdatetime(1912, 7, 29), "%G年%m月%d日", "明治45年07月29日"),
            (jpdatetime(1912, 7, 29), "%-G年%m月%d日", "明治45年07月29日"),
            (jpdatetime(1868, 9, 8), "%G年%m月%d日", "明治元年09月08日"),
            (jpdatetime(1868, 9, 8), "%-G年%m月%d日", "明治元年09月08日"),
        ]

        # Test cases for strftime with %g format (Abbreviated Japanese Era Name)
        self.test_cases_strftime_g = [
            # Reiwa Era
            (jpdatetime(2023, 10, 30), "%g年%m月%d日", "令05年10月30日"),
            (jpdatetime(2023, 10, 30), "%-g年%m月%d日", "令5年10月30日"),
            (jpdatetime(2019, 5, 1), "%g年%m月%d日", "令01年05月01日"),
            (jpdatetime(2019, 5, 1), "%-g年%m月%d日", "令1年05月01日"),
            # Heisei Era
            (jpdatetime(2018, 4, 1), "%g年%m月%d日", "平30年04月01日"),
            (jpdatetime(2018, 4, 1), "%-g年%m月%d日", "平30年04月01日"),
            (jpdatetime(1989, 1, 8), "%g年%m月%d日", "平01年01月08日"),
            (jpdatetime(1989, 1, 8), "%-g年%m月%d日", "平1年01月08日"),
            # Showa Era
            (jpdatetime(1989, 1, 7), "%g年%m月%d日", "昭64年01月07日"),
            (jpdatetime(1989, 1, 7), "%-g年%m月%d日", "昭64年01月07日"),
            (jpdatetime(1926, 12, 25), "%g年%m月%d日", "昭01年12月25日"),
            (jpdatetime(1926, 12, 25), "%-g年%m月%d日", "昭1年12月25日"),
            # Taisho Era
            (jpdatetime(1926, 12, 24), "%g年%m月%d日", "大15年12月24日"),
            (jpdatetime(1926, 12, 24), "%-g年%m月%d日", "大15年12月24日"),
            (jpdatetime(1912, 7, 30), "%g年%m月%d日", "大01年07月30日"),
            (jpdatetime(1912, 7, 30), "%-g年%m月%d日", "大1年07月30日"),
            # Meiji Era
            (jpdatetime(1912, 7, 29), "%g年%m月%d日", "明45年07月29日"),
            (jpdatetime(1912, 7, 29), "%-g年%m月%d日", "明45年07月29日"),
            (jpdatetime(1868, 9, 8), "%g年%m月%d日", "明01年09月08日"),
            (jpdatetime(1868, 9, 8), "%-g年%m月%d日", "明1年09月08日"),
        ]

        # Test cases for strftime with %E format (Full English Era Name)
        self.test_cases_strftime_E = [
            # Reiwa Era
            (jpdatetime(2023, 10, 30), "%E, %B %d", "Reiwa 05, October 30"),
            (jpdatetime(2023, 10, 30), "%-E, %B %d", "Reiwa 5, October 30"),
            (jpdatetime(2019, 5, 1), "%E, %B %d", "Reiwa 01, May 01"),
            (jpdatetime(2019, 5, 1), "%-E, %B %d", "Reiwa 1, May 01"),
            # Heisei Era
            (jpdatetime(2018, 4, 1), "%E, %B %d", "Heisei 30, April 01"),
            (jpdatetime(2018, 4, 1), "%-E, %B %d", "Heisei 30, April 01"),
            (jpdatetime(1989, 1, 8), "%E, %B %d", "Heisei 01, January 08"),
            (jpdatetime(1989, 1, 8), "%-E, %B %d", "Heisei 1, January 08"),
            # Showa Era
            (jpdatetime(1989, 1, 7), "%E, %B %d", "Showa 64, January 07"),
            (jpdatetime(1989, 1, 7), "%-E, %B %d", "Showa 64, January 07"),
            (jpdatetime(1926, 12, 25), "%E, %B %d", "Showa 01, December 25"),
            (jpdatetime(1926, 12, 25), "%-E, %B %d", "Showa 1, December 25"),
            # Taisho Era
            (jpdatetime(1926, 12, 24), "%E, %B %d", "Taisho 15, December 24"),
            (jpdatetime(1926, 12, 24), "%-E, %B %d", "Taisho 15, December 24"),
            (jpdatetime(1912, 7, 30), "%E, %B %d", "Taisho 01, July 30"),
            (jpdatetime(1912, 7, 30), "%-E, %B %d", "Taisho 1, July 30"),
            # Meiji Era
            (jpdatetime(1912, 7, 29), "%E, %B %d", "Meiji 45, July 29"),
            (jpdatetime(1912, 7, 29), "%-E, %B %d", "Meiji 45, July 29"),
            (jpdatetime(1868, 9, 8), "%E, %B %d", "Meiji 01, September 08"),
            (jpdatetime(1868, 9, 8), "%-E, %B %d", "Meiji 1, September 08"),
        ]

        # Test cases for strftime with %e format (Abbreviated English Era Name)
        self.test_cases_strftime_e = [
            # Reiwa Era
            (jpdatetime(2023, 10, 30), "%e/%m/%d", "R05/10/30"),
            (jpdatetime(2023, 10, 30), "%-e/%m/%d", "R5/10/30"),
            (jpdatetime(2019, 5, 1), "%e/%m/%d", "R01/05/01"),
            (jpdatetime(2019, 5, 1), "%-e/%m/%d", "R1/05/01"),
            # Heisei Era
            (jpdatetime(2018, 4, 1), "%e/%m/%d", "H30/04/01"),
            (jpdatetime(2018, 4, 1), "%-e/%m/%d", "H30/04/01"),
            (jpdatetime(1989, 1, 8), "%e/%m/%d", "H01/01/08"),
            (jpdatetime(1989, 1, 8), "%-e/%m/%d", "H1/01/08"),
            # Showa Era
            (jpdatetime(1989, 1, 7), "%e/%m/%d", "S64/01/07"),
            (jpdatetime(1989, 1, 7), "%-e/%m/%d", "S64/01/07"),
            (jpdatetime(1926, 12, 25), "%e/%m/%d", "S01/12/25"),
            (jpdatetime(1926, 12, 25), "%-e/%m/%d", "S1/12/25"),
            # Taisho Era
            (jpdatetime(1926, 12, 24), "%e/%m/%d", "T15/12/24"),
            (jpdatetime(1926, 12, 24), "%-e/%m/%d", "T15/12/24"),
            (jpdatetime(1912, 7, 30), "%e/%m/%d", "T01/07/30"),
            (jpdatetime(1912, 7, 30), "%-e/%m/%d", "T1/07/30"),
            # Meiji Era
            (jpdatetime(1912, 7, 29), "%e/%m/%d", "M45/07/29"),
            (jpdatetime(1912, 7, 29), "%-e/%m/%d", "M45/07/29"),
            (jpdatetime(1868, 9, 8), "%e/%m/%d", "M01/09/08"),
            (jpdatetime(1868, 9, 8), "%-e/%m/%d", "M1/09/08"),
        ]

        # Test cases for strptime with %G format
        self.test_cases_strptime_G = [
            # Reiwa Era
            ("令和05年10月30日", "%G年%m月%d日", jpdatetime(2023, 10, 30)),
            ("令和5年10月30日", "%-G年%m月%d日", jpdatetime(2023, 10, 30)),
            ("令和元年05月01日", "%G年%m月%d日", jpdatetime(2019, 5, 1)),
            ("令和元年05月01日", "%-G年%m月%d日", jpdatetime(2019, 5, 1)),
            # Heisei Era
            ("平成30年04月01日", "%G年%m月%d日", jpdatetime(2018, 4, 1)),
            ("平成30年04月01日", "%-G年%m月%d日", jpdatetime(2018, 4, 1)),
            ("平成元年01月08日", "%G年%m月%d日", jpdatetime(1989, 1, 8)),
            ("平成元年01月08日", "%-G年%m月%d日", jpdatetime(1989, 1, 8)),
            # Showa Era
            ("昭和64年01月07日", "%G年%m月%d日", jpdatetime(1989, 1, 7)),
            ("昭和64年01月07日", "%-G年%m月%d日", jpdatetime(1989, 1, 7)),
            ("昭和元年12月25日", "%G年%m月%d日", jpdatetime(1926, 12, 25)),
            ("昭和元年12月25日", "%-G年%m月%d日", jpdatetime(1926, 12, 25)),
            # Taisho Era
            ("大正15年12月24日", "%G年%m月%d日", jpdatetime(1926, 12, 24)),
            ("大正15年12月24日", "%-G年%m月%d日", jpdatetime(1926, 12, 24)),
            ("大正元年07月30日", "%G年%m月%d日", jpdatetime(1912, 7, 30)),
            ("大正元年07月30日", "%-G年%m月%d日", jpdatetime(1912, 7, 30)),
            # Meiji Era
            ("明治45年07月29日", "%G年%m月%d日", jpdatetime(1912, 7, 29)),
            ("明治45年07月29日", "%-G年%m月%d日", jpdatetime(1912, 7, 29)),
            ("明治元年09月08日", "%G年%m月%d日", jpdatetime(1868, 9, 8)),
            ("明治元年09月08日", "%-G年%m月%d日", jpdatetime(1868, 9, 8)),
        ]

        # Similar test cases for strptime with %g, %E, %e
        # Test cases for strptime with %g format
        self.test_cases_strptime_g = [
            # Reiwa Era
            ("令05年10月30日", "%g年%m月%d日", jpdatetime(2023, 10, 30)),
            ("令5年10月30日", "%-g年%m月%d日", jpdatetime(2023, 10, 30)),
            ("令01年05月01日", "%g年%m月%d日", jpdatetime(2019, 5, 1)),
            ("令1年05月01日", "%-g年%m月%d日", jpdatetime(2019, 5, 1)),
            # Heisei Era
            ("平30年04月01日", "%g年%m月%d日", jpdatetime(2018, 4, 1)),
            ("平30年04月01日", "%-g年%m月%d日", jpdatetime(2018, 4, 1)),
            ("平01年01月08日", "%g年%m月%d日", jpdatetime(1989, 1, 8)),
            ("平1年01月08日", "%-g年%m月%d日", jpdatetime(1989, 1, 8)),
            # Showa Era
            ("昭64年01月07日", "%g年%m月%d日", jpdatetime(1989, 1, 7)),
            ("昭64年01月07日", "%-g年%m月%d日", jpdatetime(1989, 1, 7)),
            ("昭01年12月25日", "%g年%m月%d日", jpdatetime(1926, 12, 25)),
            ("昭1年12月25日", "%-g年%m月%d日", jpdatetime(1926, 12, 25)),
            # Taisho Era
            ("大15年12月24日", "%g年%m月%d日", jpdatetime(1926, 12, 24)),
            ("大15年12月24日", "%-g年%m月%d日", jpdatetime(1926, 12, 24)),
            ("大01年07月30日", "%g年%m月%d日", jpdatetime(1912, 7, 30)),
            ("大1年07月30日", "%-g年%m月%d日", jpdatetime(1912, 7, 30)),
            # Meiji Era
            ("明45年07月29日", "%g年%m月%d日", jpdatetime(1912, 7, 29)),
            ("明45年07月29日", "%-g年%m月%d日", jpdatetime(1912, 7, 29)),
            ("明01年09月08日", "%g年%m月%d日", jpdatetime(1868, 9, 8)),
            ("明1年09月08日", "%-g年%m月%d日", jpdatetime(1868, 9, 8)),
        ]

        # Test cases for strptime with %E format
        self.test_cases_strptime_E = [
            # Reiwa Era
            ("Reiwa 05, October 30", "%E, %B %d", jpdatetime(2023, 10, 30)),
            ("Reiwa 5, October 30", "%-E, %B %d", jpdatetime(2023, 10, 30)),
            ("Reiwa 01, May 01", "%E, %B %d", jpdatetime(2019, 5, 1)),
            ("Reiwa 1, May 01", "%-E, %B %d", jpdatetime(2019, 5, 1)),
            # Heisei Era
            ("Heisei 30, April 01", "%E, %B %d", jpdatetime(2018, 4, 1)),
            ("Heisei 30, April 01", "%-E, %B %d", jpdatetime(2018, 4, 1)),
            ("Heisei 01, January 08", "%E, %B %d", jpdatetime(1989, 1, 8)),
            ("Heisei 1, January 08", "%-E, %B %d", jpdatetime(1989, 1, 8)),
            # Showa Era
            ("Showa 64, January 07", "%E, %B %d", jpdatetime(1989, 1, 7)),
            ("Showa 64, January 07", "%-E, %B %d", jpdatetime(1989, 1, 7)),
            ("Showa 01, December 25", "%E, %B %d", jpdatetime(1926, 12, 25)),
            ("Showa 1, December 25", "%-E, %B %d", jpdatetime(1926, 12, 25)),
            # Taisho Era
            ("Taisho 15, December 24", "%E, %B %d", jpdatetime(1926, 12, 24)),
            ("Taisho 15, December 24", "%-E, %B %d", jpdatetime(1926, 12, 24)),
            ("Taisho 01, July 30", "%E, %B %d", jpdatetime(1912, 7, 30)),
            ("Taisho 1, July 30", "%-E, %B %d", jpdatetime(1912, 7, 30)),
            # Meiji Era
            ("Meiji 45, July 29", "%E, %B %d", jpdatetime(1912, 7, 29)),
            ("Meiji 45, July 29", "%-E, %B %d", jpdatetime(1912, 7, 29)),
            ("Meiji 01, September 08", "%E, %B %d", jpdatetime(1868, 9, 8)),
            ("Meiji 1, September 08", "%-E, %B %d", jpdatetime(1868, 9, 8)),
        ]

        # Test cases for strptime with %e format
        self.test_cases_strptime_e = [
            # Reiwa Era
            ("R05/10/30", "%e/%m/%d", jpdatetime(2023, 10, 30)),
            ("R5/10/30", "%-e/%m/%d", jpdatetime(2023, 10, 30)),
            ("R01/05/01", "%e/%m/%d", jpdatetime(2019, 5, 1)),
            ("R1/05/01", "%-e/%m/%d", jpdatetime(2019, 5, 1)),
            # Heisei Era
            ("H30/04/01", "%e/%m/%d", jpdatetime(2018, 4, 1)),
            ("H30/04/01", "%-e/%m/%d", jpdatetime(2018, 4, 1)),
            ("H01/01/08", "%e/%m/%d", jpdatetime(1989, 1, 8)),
            ("H1/01/08", "%-e/%m/%d", jpdatetime(1989, 1, 8)),
            # Showa Era
            ("S64/01/07", "%e/%m/%d", jpdatetime(1989, 1, 7)),
            ("S64/01/07", "%-e/%m/%d", jpdatetime(1989, 1, 7)),
            ("S01/12/25", "%e/%m/%d", jpdatetime(1926, 12, 25)),
            ("S1/12/25", "%-e/%m/%d", jpdatetime(1926, 12, 25)),
            # Taisho Era
            ("T15/12/24", "%e/%m/%d", jpdatetime(1926, 12, 24)),
            ("T15/12/24", "%-e/%m/%d", jpdatetime(1926, 12, 24)),
            ("T01/07/30", "%e/%m/%d", jpdatetime(1912, 7, 30)),
            ("T1/07/30", "%-e/%m/%d", jpdatetime(1912, 7, 30)),
            # Meiji Era
            ("M45/07/29", "%e/%m/%d", jpdatetime(1912, 7, 29)),
            ("M45/07/29", "%-e/%m/%d", jpdatetime(1912, 7, 29)),
            ("M01/09/08", "%e/%m/%d", jpdatetime(1868, 9, 8)),
            ("M1/09/08", "%-e/%m/%d", jpdatetime(1868, 9, 8)),
        ]

    def test_strftime_full_jpEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_G:
            with self.subTest(date=date, format_string=format_string):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strftime_abbr_jpEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_g:
            with self.subTest(date=date, format_string=format_string):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strftime_full_enEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_E:
            with self.subTest(date=date, format_string=format_string):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strftime_abbr_enEra(self):
        for date, format_string, expected_output in self.test_cases_strftime_e:
            with self.subTest(date=date, format_string=format_string):
                self.assertEqual(date.strftime(format_string), expected_output)

    def test_strptime_full_jpEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_G:
            with self.subTest(date_string=date_string, format_string=format_string):
                result = jpdatetime.strptime(date_string, format_string)
                self.assertEqual(result, expected_date)

    def test_strptime_abbr_jpEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_g:
            with self.subTest(date_string=date_string, format_string=format_string):
                result = jpdatetime.strptime(date_string, format_string)
                self.assertEqual(result, expected_date)

    def test_strptime_full_enEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_E:
            with self.subTest(date_string=date_string, format_string=format_string):
                result = jpdatetime.strptime(date_string, format_string)
                self.assertEqual(result, expected_date)

    def test_strptime_abbr_enEra(self):
        for date_string, format_string, expected_date in self.test_cases_strptime_e:
            with self.subTest(date_string=date_string, format_string=format_string):
                result = jpdatetime.strptime(date_string, format_string)
                self.assertEqual(result, expected_date)

if __name__ == "__main__":
    unittest.main()
