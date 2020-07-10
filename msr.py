import argparse
import faster_than_requests as requests


# Constants
VERSION = '0.1.0'


# Parse arguments
parser = argparse.ArgumentParser(description="Store your URL's")

parser.add_argument("-v", "--version", action="store_true", help="print current version of script")

args = parser.parse_args()


# Get or create sqlite db

# Define Functions

# Execute arguments

if args.version:
	print(VERSION)