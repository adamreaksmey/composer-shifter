import os

def getComposerVersions():
    current_directory = os.path.abspath(os.curdir)
    parent_directory = os.path.dirname(current_directory)
    composers_folder = os.path.join(parent_directory, 'composers')

    if not os.path.exists(composers_folder):
        print("You don't have any composer versions installed!")
        return []

    composer_contents = []
    for item in os.listdir(composers_folder):
        item_path = os.path.join(composers_folder, item)
        composer_contents.append(os.path.basename(item_path))
    return composer_contents

def checkInstalledVersion(version):
    _allV = getComposerVersions()
    if version in _allV:
        print('test dev')
