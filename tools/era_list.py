import json
import os
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_era_list(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def hiragana_to_romaji(hiragana):
    romaji_map = {
        'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
        'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
        'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
        'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
        'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
        'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
        'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
        'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
        'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
        'わ': 'wa', 'を': 'wo', 'ん': 'n\'',
        'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
        'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
        'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
        'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
        'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
        'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
        'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
        'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
        'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
        'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
        'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
        'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
        'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
        'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
        'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
        'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po'
    }
    romaji = ""
    i = 0
    while i < len(hiragana):
        if i + 1 < len(hiragana) and hiragana[i:i+2] in romaji_map:
            romaji += romaji_map[hiragana[i:i+2]]
            i += 2
        else:
            romaji += romaji_map.get(hiragana[i], hiragana[i])
            i += 1
    romaji = re.sub(r"n'(?=[bcdfghjklmnpqrstvwxyz]|$)", "n", romaji)
    romaji = romaji.replace("ou", "ō")
    romaji = romaji.replace("uu", "ū")
    return romaji[0].upper() + romaji[1:]

def extract_era_data(row):
    if row.find('th') and len(row.find_all('td')) in [5, 6]:
        era_name = row.find('th').get_text(strip=True)
        era_furigana = row.find_all('td')[0].get_text(strip=True)
        era_furigana_romaji = hiragana_to_romaji(era_furigana)
        era_from = row.find_all('td')[1].get_text(strip=True)
        date_match = re.search(r'(\d{3,4})年(\d{1,2})月(\d{1,2})日', era_from)
        if date_match:
            year, month, day = date_match.groups()
            date_text = f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
            return {"name_ja": era_name, "name_en": era_furigana_romaji, "start_date": date_text}
    elif len(row.find_all('td')) == 8:
        era_name = row.select_one("td > b > a").text
        era_furigana = row.find_all('td')[0].get_text(strip=True)
        date_match = re.search(r'[\u3040-\u309F]+', era_furigana)
        if date_match:
            era_furigana = date_match.group(0)
        era_furigana_romaji = hiragana_to_romaji(era_furigana)
        era_from = row.find_all('td')[1].get_text(strip=True)
        date_match = re.search(r'（?(\d{4})年）?(\d{1,2})月(\d{1,2})日', era_from)
        if date_match:
            year, month, day = date_match.groups()
            date_text = f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
            return {"name_ja": era_name, "name_en": era_furigana_romaji, "start_date": date_text}
    return None

def parse_era_tables(tables):
    era_list = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:
            if len(row.find_all('td')) in [5, 6, 8]:
                era_data = extract_era_data(row)
                if era_data:
                    era_list.append(era_data)
    return era_list

def remove_unwanted_eras(era_list, delete_list):
    return [era for era in era_list if era["name_ja"] not in delete_list]

def save_eras_to_json(era_list, file_path):
    json_output = json.dumps(era_list, ensure_ascii=False, indent=4)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_output)

if __name__ == "__main__":
    url = "https://ja.wikipedia.org/wiki/元号一覧_(日本)"
    soup = fetch_wikipedia_era_list(url)
    tables = soup.find_all('table', {'class': 'wikitable'})
    era_list = parse_era_tables(tables)
    era_list.reverse()
    delete_list = ["-", "大化", "白雉", "朱鳥", "大宝", "慶雲", "和銅"]
    era_list = remove_unwanted_eras(era_list, delete_list)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../jpdatetime/eras.json")
    save_eras_to_json(era_list, file_path)
