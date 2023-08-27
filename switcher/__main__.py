from switcher.versions import getComposerVersions

def checkInstalledVersion(version):
    _allV = getComposerVersions()
    if version in _allV:
        print('test dev')
    else:
        print(f'Composer v: {version} not found!')
