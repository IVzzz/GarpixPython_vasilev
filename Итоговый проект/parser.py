import requests


def find_all_url(s, open_word, close_word):
    word = s
    url_list = []
    while word.count(close_word) > 0:
        end_url = word.index(close_word) + len(close_word)
        start_url = word[:end_url].rfind(open_word) + 1
        url_list.append(word[start_url:end_url])
        word = word[end_url:]
    return url_list


if __name__ == '__main__':
    open_word = '"'
    img_types = ['.jpg', '.png', '.svg', '.webp']
    img_counter = 0
    url = input()
    if url[-1] == '/':
        url = url[:len(url) - 1]

    response = requests.get(url)
    content = str(response.content)
    paths = []
    for t in img_types:
        paths += find_all_url(content, open_word, t)
    paths = set(paths)
    paths = list(paths)
    for img_url in paths:
        if img_url[0] == '/':
            img_url = url + img_url
        try:
            img_response = requests.get(img_url)
        except:
            continue
        if img_response.status_code >= 400:
            continue
        img_counter += 1
        with open(f'images/image{img_counter}.jpg', 'wb') as fp:
            fp.write(img_response.content)