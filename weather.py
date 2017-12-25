import os
import requests
import json
import click
import colorama
from colorama import Fore, Back, Style

def print_json(json_block, sort=True, indents=4):
    if type(json_block) is str:
        print(json.dumps(json.loads(json_block), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_block, sort_keys=sort, indent=indents))

    return None

def print_current_weather(location, api_key, units, json, query):
    owm_api_url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
        'units': units
    }

    response = requests.get(owm_api_url, params=query_params)

    if query:
        print(f"{Fore.YELLOW}api query: {Fore.WHITE}{response.url}")

    if json:
        print(f"{Fore.YELLOW}response json:")
        print_json(response.json())
    else:
        if response.json()['cod'] is not 200:
            print(f"{Fore.RED}error:")
            print_json(response.json())
            exit()

        name = response.json()['name']
        country = response.json()['sys']['country']
        temp = response.json()['main']['temp']
        weather = response.json()['weather'][0]['description']

        temp_unit = 'K'
        if units == "metric":
            temp_unit = 'C'
        elif units == "imperial":
            temp_unit = 'F'

        pad_to = 13
        print("{0}{1:<{2}s}{3}{4}".format(Fore.MAGENTA, "location:", pad_to, Fore.WHITE, name))
        print("{0}{1:<{2}s}{3}{4}".format(Fore.BLUE, "country:", pad_to, Fore.WHITE, country))
        print("{0}{1:<{2}s}{3}{4:.1f}°{5}".format(Fore.GREEN, "temperature:", pad_to, Fore.WHITE, \
            temp, temp_unit))
        print("{0}{1:<{2}s}{3}{4}".format(Fore.CYAN, "weather:", pad_to, Fore.WHITE, weather))

@click.command()
@click.argument('location')
@click.option(
    '--api-key', '-a',
    help='open weather map api key'
)
@click.option(
    '--units', '-u', default='metric',
    type=click.Choice(['standard', 'metric', 'imperial']),
    help='units of measurement '
)
@click.option(
    '--json', '-j', is_flag=True,
    help='print json response'
)
@click.option(
    '--query', '-q', is_flag=True,
    help='print api query'
)
def main(location, api_key, units, json, query):
    """
    A simple weather script using the open weather map api. Location accepts a town/city name and
    optionally a country code. e.g 'Melbourne' or 'Melbourne, AU'

    API reference: http://openweathermap.org/api
    """
    colorama.init(autoreset=True)

    if api_key:
        owm_api_key = api_key
    else:
        owm_api_key = os.environ.get('OPENWEATHERMAP_KEY', 'None')

    print_current_weather(location, owm_api_key, units, json, query)

if __name__ == "__main__":
    main()
