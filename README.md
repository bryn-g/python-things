# python-things

🐍 Pieces of Python code and things.
#### text_colorizer.py
```python (3.6)``` ```click (6.7)```

Uses a class called IroList to save colors by label. The word 'iro' is Japanese romanji for color.
```sh
Usage: text_colorizer.py [OPTIONS]

  A simple script to colorize text using ansi or terminal color codes.

Options:
  -txt, --text TEXT  example colorizer text
  -t, --tables       print ansi color tables
  --help             Show this message and exit.
```
```sh
ansi colorizer examples

ansi_colorizer.iro(text, 'pinkbg'): This is a test.
ansi_colorizer.set_iro: pink
ansi_colorizer.iro(text): This is a test.
ansi iro list: {'pinkbg': ['\x1b[7;35;47m', '\x1b[0m'], 'pink': ['\x1b[1;35m', '\x1b[0m']}

term colorizer examples

term_colorizer.iro(text, 'orange'): This is a test.
term_colorizer.iro(text, 'redbg'): This is a test.
term_colorizer.set_iro: orange
term_colorizer.iro(text): This is a test.
term iro list: {'orange': ['\x1b[38;5;172m', '\x1b[0m'], 'redbg': ['\x1b[48;5;197m', '\x1b[0m']}
```
#### random_text_colorizer.py
```python (3.6)``` ```click (6.7)``` ```colorama (0.3.9)```
```sh
Usage: random_text_colorizer.py [OPTIONS] TEXT

  A simple script to randomly colorize text.

Options:
  -b, --back   include back colors
  -w, --words  color words instead of letters
  -c, --case   randomize case of letters
  --help       Show this message and exit.
```
#### weather.py
```python (3.6)``` ```click (6.7)``` ```colorama (0.3.9)```

Based on [Writing CLI Tools with Click](https://dbader.org/blog/python-commandline-tools-with-click) tutorial by Seb Vetter.
```sh
Usage: weather.py [OPTIONS] LOCATION

  A simple weather script using the open weather map api. Location accepts a
  town/city name and optionally an ISO 3166 country code. e.g 'Melbourne' or
  'Melbourne, AU'

  API reference: http://openweathermap.org/api

Options:
  -a, --api-key TEXT              open weather map api key
  -u, --units [standard|metric|imperial]
                                  units of measurement
  -t, --time [local|utc]          print local or utc time
  -j, --json                      print json response
  -q, --query                     print api query
  --help                          Show this message and exit.

$ python weather.py Melbourne
location:    Melbourne
country:     AU
time:        2017-12-25 20:00 (local)
temperature: 17.3°C
weather:     clear sky
wind:        7.7 m/s
```
