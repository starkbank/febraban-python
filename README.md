## Deployment instructions

### Global
Before deployment, change the project _version_ on `setup.py` file and set the correct _download_url_.
Then make sure you have the file `~/.pypirc` with the content below and the correct credentials instead of the provided placeholders:
```
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
```

### Test environment
Run ```python setup.py sdist upload -r pypitest``` inside the project directory.

### Live environment
Run ```python setup.py sdist upload -r pypi``` inside the project directory.
