import requests


def send_request(url, params):
    response = requests.get(url, params=params)
    return response
