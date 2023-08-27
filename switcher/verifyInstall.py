from switcher.versions import getComposerVersions

def checkInstalledVersion(version):
    _allV = getComposerVersions(version)
    if version == "see_installed":
        return _allV;
    if version in _allV:
        print(f'Composer v: {version} found!')
        return True
    else:
        print(f'Composer v: {version} not found!')
        return False
