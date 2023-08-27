import os

def terminalInitial(props):
    options = {
        "1": props["download_single"],
        "2": props["download_all"],
        "3": props["switch_version"],
        "4" : props["see_installed"]
    }

    os.system('cls' if os.name == 'nt' else 'clear')
    question = """
What would you like to do?:
Please input a number:
1. Download a single composer version
2. Download all composer versions
3. Switch composer version
4. See your installed composer versions
    """
    print(question)
    selection = input("Please choose a number: ")
    options.get(selection, props["invalid_option"])()