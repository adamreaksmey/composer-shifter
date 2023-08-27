from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def versionScraper(_version):
    url = 'https://getcomposer.org/download/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    composer_links = [
        urljoin(url, link['href'])
        for link in links
        if 'composer.phar' in link.get('href') and
        link.get('href').endswith('composer.phar') and
        ('latest' not in link.get('href') and (
            not _version or _version in link.get('href')))
    ]

    return composer_links;
