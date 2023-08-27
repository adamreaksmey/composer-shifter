from switcher.verifyInstall import checkInstalledVersion
import os
import shutil

def switchV1(_version):
    if checkInstalledVersion(_version) and not (_version == "see_installed"):
        try:
            current_directory = os.path.abspath(os.curdir)
            parent_directory = os.path.dirname(current_directory)
            composers_folder = os.path.join(parent_directory, f'composer-switcher\\composers\\{_version}')
            file = "composer.phar"
            source_path = os.path.join(composers_folder, file)
            destination_path = os.path.join("C:\\composer", file)
            shutil.copy2(source_path, destination_path)
            print("Composer successfully switched to", _version)
        except Exception as e:
            print(e)
        return;
    
    if _version == "see_installed":
        for item in checkInstalledVersion(_version):
            print(f'Composer: {item}')
        return


        
