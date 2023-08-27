from downloader.__main__ import initComposerDownload
from switcher.__main__ import checkInstalledVersion
from components.terminal_init.__main__ import terminalInitial

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

terminalInitial({
    "download_single" : download_single,
    "download_all" : download_all,
    "switch_version" : switch_version,
    "invalid_option": invalid_option,
})

