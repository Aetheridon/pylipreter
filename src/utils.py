'''Utilities such as reading source code.'''
from pathlib import Path

def read_source(path):
    try:
        return Path(path).read_text()
    except FileNotFoundError:
        print(f"File at path {path} not found!\n")
        exit(1)
    except Exception as e:
        print(f"Got error whilst trying to read source file: {e}\n")
        exit(1)