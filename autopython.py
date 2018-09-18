import os
import collections
import argparse
import re
import subprocess


def create_file(path, content):
    with open(path, 'a+') as f:
        f.write(content)


def generate_structure(files):
    for f in files:
        if not os.path.exists(f.path):
            os.makedirs(f.path)
        create_file("{path}/{file}".format(path=f.path,
                                           file=f.file), f.content)


def main():
    parser = argparse.ArgumentParser(
        description='Creates Python project structure')
    parser.add_argument('name', type=str, help='Name of your application')
    parser.add_argument('--pipenv', dest='pipenv', action='store_true')
    parser.add_argument('--no-pipenv', dest='pipenv', action='store_false')
    parser.set_defaults(feature=True)

    args = parser.parse_args()

    name = re.sub(r"\s+", '-', args.name).lower()
    File = collections.namedtuple("File", ["path", "file", "content"])

    files = [

        File("./{}".format(name), "__init__.py", "from . import utils"),
        File("./{}".format(name), "{}.py".format(name), "from . import helpers"),
        File("./{}".format(name), "helpers.py", "# helper functions"),
        File("./test", "test_basics.py", "# Tests"),
        File(".", "setup.py", "# setup.py"),
        File(".", "README.md", "# Sample")

    ]

    generate_structure(files)

    if args.pipenv:
        subprocess.call(['pipenv', 'install'])


if __name__ == '__main__':
    main()
