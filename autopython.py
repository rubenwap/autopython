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


import argparse
import collections
import os
import re
import subprocess


def create_file(path, content):
    """Creates a file. Essential functionality for this template generation"""
    with open(path, 'a+') as file:
        file.write(content)

def generate_structure(files):
    """Generates the structure based on the list of files provided"""
    for file in files:
        if not os.path.exists(file.path):
            os.makedirs(file.path)
        create_file("{path}/{file}".format(path=file.path,
                                           file=file.file), file.content)


def main():
    """Runs the main set of actions"""
    parser = argparse.ArgumentParser(
        description='Creates Python project structure')
    parser.add_argument('name', type=str, help='Name of your application')
    parser.add_argument('--pipenv', dest='pipenv', action='store_true')
    parser.add_argument('--no-pipenv', dest='pipenv', action='store_false')
    parser.set_defaults(feature=True)

    args = parser.parse_args()

    name = re.sub(r"\s+", '-', args.name).lower()
    auto_file = collections.namedtuple("File", ["path", "file", "content"])

    files = [

        auto_file("./{}".format(name), "__init__.py", "from . import utils"),
        auto_file("./{}".format(name), "{}.py".format(name), "from . import helpers"),
        auto_file("./{}".format(name), "helpers.py", "# helper functions"),
        auto_file("./test", "test_basics.py", "# Tests"),
        auto_file(".", "setup.py", "# setup.py"),
        auto_file(".", "README.md", "# Sample")

    ]

    generate_structure(files)

    if args.pipenv:
        subprocess.call(['pipenv', 'install'])


if __name__ == '__main__':
    main()
