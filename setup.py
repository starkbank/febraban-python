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
    url='https://github.com/HummingbirdStudio/febraban.git',
    author="Hummingbird Product Studio",
    author_email="rafael.castro@hummingbird.com.br",
    keywords=["febraban", "cnab", "transfer", "billing", "bank", "cnab240", "febraban240"],
    version = "0.1.14"
)