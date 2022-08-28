import requests


def send_request(url):
    response = requests.get(url)
    return {"url": url, "status": response.status_code}
