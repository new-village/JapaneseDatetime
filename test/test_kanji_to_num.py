import unittest
from jpdatetime.kanji_to_num import replace_kanji_numerals

class TestReplaceKanjiNumerals(unittest.TestCase):
    def test_single_digits(self):
        test_cases = [
            ('一', '1'),
            ('二', '2'),
            ('三', '3'),
            ('四', '4'),
            ('五', '5'),
            ('六', '6'),
            ('七', '7'),
            ('八', '8'),
            ('九', '9'),
            ('零', '0'),
            ('〇', '0'),
        ]
        for kanji, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji), expected)
    
    def test_ten(self):
        self.assertEqual(replace_kanji_numerals('十'), '10')
    
    def test_numbers_11_to_19(self):
        test_cases = [
            ('十一', '11'),
            ('十二', '12'),
            ('十三', '13'),
            ('十四', '14'),
            ('十五', '15'),
            ('十六', '16'),
            ('十七', '17'),
            ('十八', '18'),
            ('十九', '19'),
        ]
        for kanji, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji), expected)
    
    def test_multiples_of_ten(self):
        test_cases = [
            ('二十', '20'),
            ('三十', '30'),
            ('四十', '40'),
            ('五十', '50'),
            ('六十', '60'),
            ('七十', '70'),
            ('八十', '80'),
            ('九十', '90'),
        ]
        for kanji, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji), expected)
    
    def test_numbers_21_to_99(self):
        test_cases = [
            ('二十一', '21'),
            ('三十二', '32'),
            ('四十三', '43'),
            ('五十四', '54'),
            ('六十五', '65'),
            ('七十六', '76'),
            ('八十七', '87'),
            ('九十八', '98'),
            ('九十九', '99'),
        ]
        for kanji, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji), expected)
    
    def test_alternative_forms(self):
        test_cases = [
            ('一〇', '10'),
            ('二〇', '20'),
            ('三〇', '30'),
            ('四〇', '40'),
            ('五〇', '50'),
            ('六〇', '60'),
            ('七〇', '70'),
            ('八〇', '80'),
            ('九〇', '90'),
            ('二一', '21'),
            ('三一', '31'),
            ('四五', '45'),
            ('五六', '56'),
        ]
        for kanji, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji), expected)
    
    def test_mixed_text(self):
        test_cases = [
            ('平成十八年六月三〇日', '平成18年6月30日'),
            ('令和二年五月一日', '令和2年5月1日'),
            ('昭和四五年一二月三一日', '昭和45年12月31日'),
            ('大正一〇年七月二〇日', '大正10年7月20日'),
            ('明治二〇年一月一日', '明治20年1月1日'),
            ('本日は令和二年二月二二日です', '本日は令和2年2月22日です'),
        ]
        for kanji_text, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji_text), expected)
    
    def test_invalid_numerals(self):
        test_cases = [
            ('百', '百'),  # '百' is not handled, remains unchanged
            ('千', '千'),      # '千' is not handled, remains unchanged
        ]
        for kanji_text, expected in test_cases:
            self.assertEqual(replace_kanji_numerals(kanji_text), expected)

if __name__ == '__main__':
    unittest.main()
