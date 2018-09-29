import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.srt")) as readme:
    README = readme.read()

setup(
    name="febraban",
    packages=find_packages(),
    include_package_data=True,
    description="A library to generate files in FEBRABAN formats",
    long_description=README,
    license="MIT License",
    url='https://github.com/starkbank/febraban.git',
    author="Stark Bank",
    author_email="developers@starkbank.com",
    keywords=["febraban", "cnab", "cnab 240", "cnab240", "febraban240", "transfer", "billing", "bank"],
    version = "0.1.21"
)