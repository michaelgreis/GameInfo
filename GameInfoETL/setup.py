from setuptools import setup

setup(name='datamartetl',
    version='1.0',
    description='All ETLs for bringing data from raw into normalized model.',
    url='https://github.com/michaelgreis/GameInfo/tree/master/GameInfoETL',
    author='Michael Greis',
    author_email='michael@letus.build',
    packages=['GameInfoEtl'],
    zip_safe=False)