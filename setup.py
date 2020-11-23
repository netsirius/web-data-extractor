# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='web_data_extractor',
    description='Web data extractor',
    version='1.0.0',
    author='Hector Santos',
    # Package dir and where parameter must be set to properly install the package
    package_dir={'': 'src'},
    packages=find_packages('src', include=['web_data_extractor*']),
    install_requires=[
        'redis==3.3.11',
        'beautifulsoup4==4.9.3',
        'requests==2.25.0',
        'html5lib==1.1',
        'pymongo==3.11.1'
    ],
    extras_require={
        "testing": [
            'pytest'
        ]
    },
    setup_requires=['pytest-runner'],
    test_suite='pytest'
)
