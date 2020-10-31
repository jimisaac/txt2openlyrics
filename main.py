import sys
from parser import Dataparser

path_to_file = input("Enter the absolute path to the .txt file: ")


def validate():
    if not path_to_file.endswith(".txt"):
        sys.exit("Program Exiting!!. The file you have entered is not in .txt format")


try:
    validate()
    files = open(path_to_file, 'r')
    input_data = files.read().split("\n\n")
    parser = Dataparser(input_data)
except FileNotFoundError as e:
    sys.exit("The file doesn't exist in the provided path")
except Exception as e:
    sys.exit("Some error has occurred in parsing the file. Check your file for syntax errors")
