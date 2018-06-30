import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")
    print(words)

    sentences = textInFile.split(".")
    sentences.remove("")

    print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return round(aveSentenceLength, 0)


userFile = input("Enter the file path to the .txt file you wish to analyze.")
userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                       "delimiters separated by spaces")
userDelimeters = userDelimeters.split(" ")
minLength = eval(input("Enter the minimum length of a word (must be a positive integer)"))
if (minLength < 1):
    minLength = 1

print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))
