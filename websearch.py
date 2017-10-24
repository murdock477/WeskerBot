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

def fourchantop():
    r = requests.get('http://boards.4chan.org/pol/')
    source_code = r.text
    supp = BeautifulSoup(source_code, 'html.parser')
    post = supp.find("a", text='Click here')
    href = post.get('href')
    full_url = ('http://boards.4chan.org/pol/' + href)
    rr = requests.get(full_url)
    source_codee = rr.text
    suppp = BeautifulSoup(source_codee, 'html.parser')
    filethumb = suppp.find('a', {'class': 'fileThumb'}).get('href')
    filethumb = filethumb.replace('//i.4cdn.org/', '/')
    full_img = 'http://i.4cdn.org'+ filethumb
    final = full_url + '\n>>>>Main Image ' + full_img
    return final

fourchantop()