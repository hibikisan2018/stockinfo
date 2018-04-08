# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='stockinfo',
    version='0.1.0',
    description='Notifying N225 and USD/JPN through LINE notify',
    long_description=readme,
    author='hibikisan2018',
    author_email='hibikisan2010@gmail.com',
    install_requires=['requests', 'bs4'],
    url='https://github.com/hibikisan2018',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
        'console_scripts':[
            'stockinfo = stockinfo.sendLineMessage2:main',
        ],
    },
)

