import requests
from collections import Counter

session = requests.Session()
URL = "https://ru.wikipedia.org/w/api.php"


def get_data(cmcontinue):
    try:
        params = {
            "action": "query",
            "cmtitle": "Категория:Животные по алфавиту",
            "cmlimit": "max",
            "list": "categorymembers",
            "format": "json",
            "cmcontinue": cmcontinue
        }
        request = session.get(url=URL, params=params)
        data = request.json()
    except:
        data = None
    return data


def get_cmcontinue(data):
    if 'continue' in data:
        cont = data['continue']['cmcontinue']
    else:
        cont = None
    return cont


def parse_animals(data):
    pages = data['query']['categorymembers']
    count_p = Counter(s['title'][0] for s in pages)
    return count_p


def main():
    counter = Counter({})
    cmcontinue = ''
    while cmcontinue != None:
        data = get_data(cmcontinue)
        cmcontinue = get_cmcontinue(data)
        animals_count = parse_animals(data)
        counter += animals_count
    return counter


wikianimals = main()
for letter in sorted(wikianimals):
    print(letter + ':', wikianimals[letter])
