"""
Returns a dictionary containing all installed packages.

return: A dictionary, key is package name value is a dictionary with
        information about package.
"""

from pip2.compat import packaging


def freeze():
    results = list(packaging.database.get_distributions(use_egg_info=True))
    installed = dict()
    for dist in results:
        installed[dist.name] = dict()
        installed[dist.name]['version'] = dist.version

    return installed
