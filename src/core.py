from utils import read_source
import sys

def main():
    if len(sys.argv) < 2:
        print("Please supply path to source")
        return 1
    source = read_source(sys.argv[1])
    print(source)

if __name__ == "__main__":
    main()
