import argparse
from hash import hashing
from compare import compare

def cli():
    parser = argparse.ArgumentParser(prog="test")
    parser.add_argument('username')
    parser.add_argument('password')
    subparser = parser.add_subparsers()
    subparser.add_parser("hash").set_defaults(func=hashing, help='writes out all data')
    subparser.add_parser("compare").set_defaults(func=compare, help='lists all names')
    args = parser.parse_args()
    args.func(args)
