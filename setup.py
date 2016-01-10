from distutils.core import setup
from Cython.Build import cythonize
import glob, os

files = []
os.chdir(".")
for file in glob.glob("*.pyx"):
    files.append(file)


setup(
    ext_modules = cythonize(files)
)
