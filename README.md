# python-things

🐍 Pieces of Python code and things.
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
