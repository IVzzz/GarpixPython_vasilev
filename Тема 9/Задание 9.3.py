import requests


def github_stat(lang_list=['python', 'c++', 'java', 'javascript', 'ruby', 'c#']):
    result = []
    url = 'https://github.com/search'
    for lang in lang_list:
        params = {'q': f'language:{lang}'}
        response = requests.get(url, params=params)
        content = str(response.text)
        start = content.index('Showing ')
        number = content[start + len('Showing '): start + len('Showing ') + content[start + len('Showing '):].index(' ')]
        number = number.replace(',', '')
        result.append([lang, int(number)])
    return result