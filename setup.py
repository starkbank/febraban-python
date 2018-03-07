import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

#Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = "0.1.11"

setup(
    name='febraban',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='A library to generate files that conform to the FEBRABAN formats',
    long_description=README,
    license="MIT License",
    author='Hummingbird Product Studio',
    author_email='deromir.neves@hummingbird.com.br',
    url='https://github.com/HummingbirdStudio/febraban.git',
    keywords=['febraban', 'cnab', 'transfer', 'billing', 'bank', 'cnab240', 'febraban240']
)