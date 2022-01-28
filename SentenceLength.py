import os
import sys


file_paths = sys.argv[1:]

def findAverageSentence(filePath, delimiters, minLength):
    try:
        file = open(filePath)
    except:
        print("This file was either invalid or not found. Please restart the program and use a proper file name.")
        exit()
    
    textInFile = file.read()

    words = textInFile.split(" ")
    # print(words)

    sentences = textInFile.split(".")
    sentences.remove("")

    # print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return round(aveSentenceLength, 0)


def main():

    if (file_paths):
        userFile = file_paths[0]
    else:
        userFile = input("Enter the file path to the .txt file you wish to analyze.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence delimiters separated by spaces")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Enter the minimum length of a word (must be a positive integer)"))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))
    input("Press enter to exit")

if __name__ == "__main__":
    main()