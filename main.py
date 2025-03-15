import sys
from stats import print_stat_report

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def main(path_to_book):
    print_stat_report(path_to_book)

main(path_to_book)