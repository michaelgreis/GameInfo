# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'SonyScraper',
    version      = '1',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = Sony.settings']},
)
