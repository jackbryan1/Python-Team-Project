import argparse
from hash import hashing


def cli():
    parser = argparse.ArgumentParser(prog="test")
    parser.add_argument('username')
    parser.add_argument('password')
    args = parser.parse_args()
    hashing(args)
