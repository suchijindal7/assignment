import requests
from bs4 import BeautifulSoup

def get_website_details(url):
    text = requests.get(url).text
    pattern = re.compile("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", re.IGNORECASE)
    print(f"Email Id: {pattern.search(text)[0]}")
    urls = re.findall('(https://www.[\w\-\.com/-]+)', text)
    print('Social Links')
    for url in urls:
        if 'facebook' in url or 'twitter' in url or 'instagram' in url or 'linkedin' in url:
            print(url)
    print('Contact Detail:')
    print(re.findall('\\d{4}[-\\.\\s]\\d{3}[-\\.\\s]\\d{3}', text))

get_website_details("https://ful.io/")
