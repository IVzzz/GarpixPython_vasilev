import requests

# не очень понял, в каком виде передается url. Это вариант, когда дают просто url и словарь с параметрами
def send_request(url, params):
    response = requests.get(url, params=params)
    return response

# это вариант, когда дан список параметров и url в виде smt.com/?param1=@&param2=@&param3=@&...
def send_request1(url, params):
    p = 0
    while url.count("@"):
        url = url.replace("@", params[p], 1)
        p += 1
    response = requests.get(url)
    return response.url
