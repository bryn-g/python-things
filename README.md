# python-things

🐍 Pieces of Python code and things.
#### weather.py
```python (3.6)``` ```click (6.7)``` ```colorama (0.3.9)```

A simple weather script using the [open weather map api](http://openweathermap.org/api).
```sh
Usage: weather.py [OPTIONS] LOCATION

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
