import requests
from bs4 import BeautifulSoup


def ytsearch(term):
    r = requests.get('https://www.youtube.com/results?search_query=' + term)
    source_code = r.text
    supp = BeautifulSoup(source_code, 'html.parser')
    result = supp.select_one("a[href*=watch?]")
    result = result.get('href')
    full_url = 'https://www.youtube.com' + result
    return full_url

