# -*- coding: utf-8 -*-
"""
This module helps with the creation of Python project templates.
Install it:
    pip install --upgrade git+https://github.com/rubenwap/autopython.git@master
And use it as:
    autopython "Name of my project" --pipenv
    or
    autopython "Name of my project" --no-pipenv
    depending on what are your pipenv needs

"""

from io import open
from os import path

from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as file:
    LONG_DESCRIPTION = file.read()

setup(

    name='autopython',
    version='1.0.1',  # Required
    description='Python template for Automation',  # Optional
    long_description=LONG_DESCRIPTION,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/rubenwap/autopython',  # Optional
    author='Ruben Sanchez',  # Optional
    # author_email='',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='template',  # Optional

    py_modules=["autopython"],

    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'autopython=autopython:main',
        ],
    },

)
