import os

def getComposerContents():
    # Get the path to the 'composers' folder
    current_directory = os.path.abspath(os.curdir)
    parent_directory = os.path.dirname(current_directory)
    composers_folder = os.path.join(parent_directory, 'composers')

    # Get all items (files and folders) within the 'composers' folder
    composer_contents = []
    for item in os.listdir(composers_folder):
        item_path = os.path.join(composers_folder, item)
        composer_contents.append(os.path.basename(item_path))
    return composer_contents

# Get and print the contents of the 'composers' folder
contents = getComposerContents()
for item in contents:
    print(item)