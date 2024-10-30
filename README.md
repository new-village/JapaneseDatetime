# JapaneseDatetime
This repository contains the `jpdatetime` class, which extends the standard Python datetime class to support Japanese era (元号) date conversions. It provides the capability to parse and format dates using Japanese eras, such as Reiwa (令和), Heisei (平成), Showa (昭和), Taisho (大正), and Meiji (明治).

## Features
* Convert Japanese era dates to Gregorian dates using the strptime method.
* Convert Gregorian dates to Japanese era formatted strings using the strftime method.
* Supports the Japanese eras: Meiji, Taisho, Showa, Heisei, and Reiwa.

## Installation
`jpdatetime` is available on pip installation.
```shell:
$ python -m pip install jpdatetime
```
  
### GitHub Install
Installing the latest version from GitHub:  
```shell:
$ git clone https://github.com/new-village/JapaneseDatetime
$ cd JapaneseDatetime
$ python setup.py install
```
    
## Usage
```pyhon:
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
```

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License.