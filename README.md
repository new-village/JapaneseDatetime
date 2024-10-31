# JapaneseDatetime
[![Test](https://github.com/new-village/cnparser/actions/workflows/test.yaml/badge.svg)](https://github.com/new-village/cnparser/actions/workflows/test.yaml)
![PyPI - Version](https://img.shields.io/pypi/v/jpdatetime)

The jpdatetime library extends Python's datetime to support Japanese eras (元号). It allows parsing and formatting dates in Japanese eras like Reiwa (令和), Heisei (平成), and more, including special support for first-year notation (元年).

## Features
* Convert Japanese era dates to Gregorian dates using the `strptime` method.
* Convert Gregorian dates to Japanese era formatted strings using the `strftime` method.
* Supports the Japanese eras: Meiji, Taisho, Showa, Heisei, and Reiwa.
* Supports the first year notation (元年) for each era.
* Allows custom formatting that includes both Japanese and Gregorian dates.

## Installation
`jpdatetime` is available for installation via pip.
```shell
$ python -m pip install jpdatetime
```
  
### GitHub Install
Installing the latest version from GitHub:  
```shell
$ git clone https://github.com/new-village/JapaneseDatetime
$ cd JapaneseDatetime
$ python setup.py install
```
    
## Usage
```python
from jpdatetime import jpdatetime

# Parsing Japanese era date string to a datetime object
date_string = "令和5年10月30日"
format_string = "%j年%m月%d日"
date_obj = jpdatetime.strptime(date_string, format_string)
print(date_obj)  # Output: 2023-10-30 00:00:00

# Formatting a datetime object to a Japanese era date string
date = jpdatetime(2024, 10, 30)
formatted_date = date.strftime("%j年%m月%d日")
print(formatted_date)  # Output: "令和6年10月30日"

# Handling the first year of an era
date_string = "令和元年5月1日"
format_string = "%j年%m月%d日"
date_obj = jpdatetime.strptime(date_string, format_string)
print(date_obj)  # Output: 2019-05-01 00:00:00

# Formatting a datetime object for the first year of an era
date = jpdatetime(2019, 5, 1)
formatted_date = date.strftime("%j年%m月%d日")
print(formatted_date)  # Output: "令和元年5月1日"
```

### Format Specifiers
- `%j`: Represents the Japanese era name and year. The format will be like "令和5" or "平成元" for the first year of the era.
- All other format specifiers (`%Y`, `%m`, `%d`, etc.) are identical to the standard `datetime` format specifiers.

## Limitation
- This library does not support Japanese eras prior to Meiji (i.e., before Meiji元年, which started on September 8, 1868).
- Date parsing and formatting are limited to the supported eras (Meiji, Taisho, Showa, Heisei, and Reiwa).
- The library does not account for dates outside of these eras or hypothetical future eras not explicitly defined.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the Apache-2.0 license.
