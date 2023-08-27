from downloader.main import initComposerDownload

if __name__ == "__main__":
    question = """
What would you like to do?:
Please input a number:
1. Download a single composer version
2. Download all composer versions
3. Switch composer version
"""
    print(question)
    selection = input("Please choose a number: ")
    if (selection == "1"):
        seeAll = input("Would you like to see all composer versions? (Y/N)")
        if (seeAll == "Y"):
            initComposerDownload('see all')
        else:
            versionNumb = input("Please input a version to download: ")
            initComposerDownload(versionNumb)
    else:
        print("test dev")
