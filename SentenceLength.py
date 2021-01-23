import os
import math

def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    #Delete new line and period characters from words list
    PrePreWords = textInFile.replace('\n', ' ')
    PreWords = PrePreWords.replace('.', '')
    words = PreWords.split(" ")

    #print(words)
    #print(len(words))

    sentences = textInFile.split(".")
    sentences.remove("")

    #print(len(sentences))

    #Check each word against specified minimum length of a word
    wordsCounted = 0
    for word in words:
        if len(word) >= minLength:
            wordsCounted = wordsCounted + 1
            continue
        else:
            continue
    #Words counted
    #print(wordsCounted)

    # print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = wordsCounted / len(sentences)
    else:
        aveSentenceLength = words

    #Round down to nearest integer
    return math.floor(aveSentenceLength)


def main():
    userFile = input("Enter the file path to the .txt file you wish to analyze.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Enter the minimum length of a word (must be a positive integer)"))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()