from downloader.__main__ import initComposerDownload
from switcher.__main__ import checkInstalledVersion
import os

def download_single():
    see_all = input("Would you like to see all available composer versions? (Y/N) ")
    if see_all.upper() == "Y":
        initComposerDownload("see all")
    version_number = input("Please input a version to download (Example: 2.5.5, 2.5.6...etc): ")
    initComposerDownload(version_number)


def download_all():
    initComposerDownload('')

def switch_version():
    checkInstalledVersion('2.5.5')
    return;

def invalid_option():
    print("Invalid option chosen. Please enter a valid number.")

options = {
    "1": download_single,
    "2": download_all,
    "3": switch_version
}

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    question = """
What would you like to do?:
Please input a number:
1. Download a single composer version
2. Download all composer versions
3. Switch composer version
"""
    print(question)
    selection = input("Please choose a number: ")
    options.get(selection, invalid_option)()
