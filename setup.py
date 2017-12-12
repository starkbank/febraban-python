from distutils.core import setup

version = "0.1.3"
setup(
    name='febraban',
    packages=['febraban'],
    version=version,
    description='A library to generate files that conform to the FEBRABAN formats',
    author='Hummingbird Product Studio',
    author_email='deromir.neves@hummingbird.com.br',
    url='https://github.com/HummingbirdStudio/febraban.git',
    download_url='https://github.com/HummingbirdStudio/febraban/archive/v%s.tar.gz' % version,
    keywords=['febraban', 'cnab', 'transfer', 'billing', 'bank']
)