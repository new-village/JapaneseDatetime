import re

def kanji_numeral_to_int(s):
    """
    Converts a kanji numeral string representing a number up to 99 into an integer.
    Supports numbers from 0 to 99.
    """
    kanji_to_num = {'零': 0, '〇': 0, '一': 1, '二': 2, '三': 3,
                    '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    if not s:
        return None
    n = len(s)
    if n == 1:
        if s == '十':
            return 10
        elif s in kanji_to_num:
            return kanji_to_num[s]
        else:
            return None
    elif n == 2:
        if s[0] == '十' and s[1] in kanji_to_num:
            # '十' + unit digit, e.g., '十三' => 10 + 3
            return 10 + kanji_to_num[s[1]]
        elif s[1] == '十' and s[0] in kanji_to_num:
            # Tens digit + '十', e.g., '三十' => 3 * 10
            return kanji_to_num[s[0]] * 10
        elif s[0] in kanji_to_num and s[1] in kanji_to_num:
            # Tens digit + units digit, e.g., '二一' => 2 * 10 + 1
            return kanji_to_num[s[0]] * 10 + kanji_to_num[s[1]]
        else:
            return None
    elif n == 3:
        if s[1] == '十' and s[0] in kanji_to_num and s[2] in kanji_to_num:
            # Tens digit + '十' + units digit, e.g., '二十三' => 2 * 10 + 3
            return kanji_to_num[s[0]] * 10 + kanji_to_num[s[2]]
        else:
            return None
    else:
        return None

def replace_kanji_numerals(text):
    """
    Replaces kanji numerals up to two digits (numbers from 0 to 99)
    in the input string with half-width Arabic numerals.
    """
    # Precompile the kanji numeral pattern
    kanji_numeral_pattern = re.compile(r'[十零〇一二三四五六七八九]{1,3}')
    
    def repl(match):
        kanji_num = match.group()
        num = kanji_numeral_to_int(kanji_num)
        if num is not None:
            return str(num)
        else:
            return kanji_num  # Leave it unchanged if cannot parse
    
    return kanji_numeral_pattern.sub(repl, text)
