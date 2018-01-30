# python-things

🐍 Pieces of Python code and things.

#### weather.py
```python (3.6)``` ```click (6.7)``` ```colorama (0.3.9)```

Based on [Writing CLI Tools with Click](https://dbader.org/blog/python-commandline-tools-with-click) tutorial by Seb Vetter.
```sh
Usage: weather.py [OPTIONS] COMMAND [ARGS]...

  A simple weather script using the open weather map api.

  API reference: http://openweathermap.org/api

Options:
  -a, --api-key TEXT  open weather map api key
  --help              Show this message and exit.

Commands:
  current  get the current weather.

python weather.py current --help
Usage: weather.py current [OPTIONS] LOCATION

  get the current weather. location can be a town/city name and optionally
  an ISO 3166 country code. e.g 'Melbourne' or 'Melbourne, AU'

Options:
  -u, --units [standard|metric|imperial]
                                  units of measurement
  -t, --time [local|utc]          print local or utc time
  -j, --json                      print json response
  -q, --query                     print api query
  --help                          Show this message and exit.

$ python weather.py current Melbourne
location:    Melbourne
country:     AU
time:        2018-01-04 10:00 (local)
temperature: 19.7°C
weather:     clear sky
wind:        3.1 m/s
```
