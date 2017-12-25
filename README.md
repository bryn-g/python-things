# python-things

🐍 Pieces of Python code and things.
#### weather.py
```python (3.6)``` ```click (6.7)``` ```colorama (0.3.9)```
```sh
Usage: weather.py [OPTIONS] LOCATION

  A simple weather script using the open weather map api. Location accepts a
  town/city name and optionally a country code. e.g 'Melbourne' or
  'Melbourne, AU'

  API reference: http://openweathermap.org/api

Options:
  -a, --api-key TEXT              open weather map api key
  -u, --units [standard|metric|imperial]
                                  units of measurement
  -j, --json                      print json response
  -q, --query                     print api query
  --help                          Show this message and exit.

$ python weather.py Melbourne
location:    Melbourne
country:     AU
temperature: 20.7°C
weather:     scattered clouds
```
