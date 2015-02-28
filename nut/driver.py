import os
import six
import sys

import argparse
import optparse

# If ../nut/__init__.py exists, add ../ to Python search path, so that
# it will override what happens to be installed in /usr/(local/)lib/python...
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                                os.pardir,
                                                os.pardir))
if os.path.exists(os.path.join(possible_topdir, 'nut', '__init__.py')):
    sys.path.insert(0, possible_topdir)

import argparse

from nut.sensor import get_data

parser = argparse.ArgumentParser(description='Robotice NUT Driver')
parser.add_argument('host', nargs='?', help='Host', default="127.0.0.1")
parser.add_argument('name', nargs='?', help='Name', default=None)
parser.add_argument(
    '-r', '--repeat', action='store_true', help="Repeat", default=False)


def pp(data):

    for datum in data:
        print str(datum)


def main():

    args = parser.parse_args()

    attrs = {
        "host": args.host,
        "name": args.name
    }
    pp(get_data(attrs))

    if args.repeat:

        while True:
            pp(get_data(attrs))

if __name__ == "__main__":
    main()
