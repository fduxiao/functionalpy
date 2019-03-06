from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='functionalpy',
    version='0.0.1',
    description='python functional programming tools',
    long_description=long_description,
    author='fduxiao',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'

        'Programming Language :: Python :: 3',
    ],


    test_suite="tests",

    packages=find_packages(exclude=["tests", "examples"]),
)
