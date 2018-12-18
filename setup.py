from os import path
from setuptools import setup, find_packages

with open(path.join(path.dirname(__file__), "README.srt")) as readme:
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
    version = "0.2.2"
)

"""
Deployment instructions
-----------------------

Global
~~~~~~

Before deployment, change the project *version* on ``setup.py`` file and
set the correct *download*\ url\_. Then make sure you have the file
``~/.pypirc`` with the content below and the correct credentials instead
of the provided placeholders:

::

    [distutils]
    index-servers =
        pypi
        pypitest

    [pypi]
    repository:https://upload.pypi.org/legacy/
    username:myusername
    password:mypassword

    [pypitest]
    repository:https://test.pypi.org/legacy/
    username:myusername
    password:mypassword


Live environment
~~~~~~~~~~~~~~~~

For unit test:

```
python -m unittest discover -s febraban/cnab240/tests -p '*Test.py'
```

For release a new version:

```
python setup.py sdist upload -r pypi`` inside the project
```

"""