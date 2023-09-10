# https://py-pkgs.org/03-how-to-package-a-python
# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_fe")