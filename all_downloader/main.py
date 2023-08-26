import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor


def download_file(url, path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(path, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=65536):
            fd.write(chunk)


def downloadAllComposersVersions():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    folder_path = os.path.join(parent_dir, 'composers')
    os.makedirs(folder_path, exist_ok=True)

    url = 'https://getcomposer.org/download/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    composer_links = [urljoin(url, link['href']) for link in links if 'composer.phar' in link.get(
        'href') and link.get('href').endswith('composer.phar') and 'latest' not in link.get('href')]

    # Download and save the composer versions
    with ThreadPoolExecutor(max_workers=5) as executor:
        for link in composer_links:
            version = link.rsplit('/', 2)[-2]
            composer_folder = os.path.join(
                folder_path, 'dev' if version == "getcomposer.org" else version)
            os.makedirs(composer_folder, exist_ok=True)

            file_path = os.path.join(composer_folder, 'composer.phar')
            executor.submit(download_file, link, file_path)
            print(f"Downloaded: {file_path}")
