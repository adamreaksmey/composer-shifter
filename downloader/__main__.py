import os
import requests
from concurrent.futures import ThreadPoolExecutor
from components.scraper.__main__ import versionScraper

def initComposerDownload(_version):
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    folder_path = os.path.join(parent_dir, 'composers')
    os.makedirs(folder_path, exist_ok=True)

    if (_version == "see all"):
        _version = ''
        composer_links = versionScraper(_version)
        for index, link in enumerate(composer_links, 1):
            print("Composer v: " + link.rsplit('/', 2)[-2])
        return;
    else:
        composer_links = versionScraper(_version)
        # Download composer
        with ThreadPoolExecutor(max_workers=5) as executor:
            for link in composer_links:
                version = link.rsplit('/', 2)[-2]
                composer_folder = os.path.join(
                    folder_path, 'dev' if version == "getcomposer.org" else version)
                os.makedirs(composer_folder, exist_ok=True)

                file_path = os.path.join(composer_folder, 'composer.phar')
                executor.submit(download_file, link, file_path)
            print(f"Composer {_version} has been downloaded!")


def download_file(url, path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(path, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=65536):
            fd.write(chunk)
