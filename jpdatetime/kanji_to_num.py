import re

# Precompute the mapping from kanji numerals to integers
kanji_to_num = {'零': 0, '〇': 0, '一': 1, '二': 2, '三': 3,
                '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
num_to_kanji = {v: k for k, v in kanji_to_num.items() if v != 0}

# Generate kanji numerals for numbers from 0 to 99
kanji_numerals = {}

# Zero representations
kanji_numerals['零'] = 0
kanji_numerals['〇'] = 0

# Numbers from 1 to 9
for i in range(1, 10):
    kanji = num_to_kanji[i]
    kanji_numerals[kanji] = i

# Number 10
kanji_numerals['十'] = 10

# Numbers from 11 to 99
for i in range(11, 100):
    tens = i // 10
    units = i % 10
    kanji = ''
    if tens > 1:
        kanji += num_to_kanji[tens]
    kanji += '十'
    if units > 0:
        kanji += num_to_kanji[units]
    kanji_numerals[kanji] = i

    # Alternative forms
    if units > 0:
        # For numbers like '二十一' or '二一'
        alt_kanji1 = num_to_kanji[tens] + '十' + num_to_kanji[units]  # e.g., '二十一'
        alt_kanji2 = num_to_kanji[tens] + num_to_kanji[units]        # e.g., '二一'
        kanji_numerals[alt_kanji1] = i
        kanji_numerals[alt_kanji2] = i
    else:
        # For multiples of ten like '二十' and '二〇'
        alt_kanji = num_to_kanji[tens] + '〇'  # e.g., '二〇'
        kanji_numerals[alt_kanji] = i

# Precompile the kanji numeral pattern, sorted by length descending to match longer numerals first
kanji_numeral_pattern = re.compile('|'.join(
    sorted(kanji_numerals.keys(), key=lambda x: -len(x))
))

def replace_kanji_numerals(text):
    """
    Replaces kanji numerals up to two digits (numbers from 0 to 99)
    in the input string with half-width Arabic numerals.
    """
    def repl(match):
        kanji_num = match.group()
        num = kanji_numerals.get(kanji_num)
        if num is not None:
            return str(num)
        else:
            return kanji_num  # Leave it unchanged if cannot parse

    return kanji_numeral_pattern.sub(repl, text)
