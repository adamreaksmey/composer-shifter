from downloader.main import initComposerDownload

if __name__ == "__main__":
    __input = input('Enter composer version to download: ')
    if (__input == "all"):
        initComposerDownload('')
    else:
        initComposerDownload(__input)
