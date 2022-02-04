from pickle import FALSE, TRUE
import requests
import json

from configparser import ConfigParser


def _get_api_key():

    """Fetch the API key from your configuration file.


    Expects a configuration file named "secrets.ini" with structure:


        [openweather]

        api_key=<YOUR-OPENWEATHER-API-KEY>

    """

    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


def isBewolk():
    # Funksie wat bepaal of dit bewolk is in Faerie Glen, al dan nie
    # Indien dit bewolk is, gee dit "True" terug
    # Indien daar geen wolke is nie, gee dit "False" terug
    # Die drempel vir bewolktheid is wolkbedekking van meer as 60%

    # Kry die API key vir die weer webwerf
    api_key = _get_api_key()
    # Stel die weer vraag op om die weer aan te vra in Faerie Glen
    query_url = 'http://api.openweathermap.org/data/2.5/forecast?q=Faerie Glen,za&mode=xml??&APPID=' + api_key
    # Vra die weer aan:
    response = requests.get(query_url)
    # Vertaal die JSON antwoord
    weather_data = json.loads(response.content)

    cloudcover = int(f"{weather_data['list'][0]['clouds']['all']}")

    if cloudcover < 60:
        #print('Inverter op sonkrag')
        return False
    else:
        #print('Wolke te veel')
        return True