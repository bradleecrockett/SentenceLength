import os

import math


def convertToString(delimiter):
    new = ""
    for x in delimiter:
        new += x
    return new


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    punctuation = ["!", "?", ":", ";", ",", "."]

    # Delete new line characters from words list
    PreWords = textInFile.replace('\n', ' ')
    words = PreWords.split(" ")
    #print(words)

    sentences = textInFile.split(".")
    sentences.remove("")
    
    # Count words that meet min length requirement
    wordsCounted = 0

    for word in words:
        # Check that ending punctuation characters aren't being factored into word length calculation
        for i in punctuation:
            if i == word[-1]:
                word = word.replace(word[-1], '')
            else:
                continue

        if len(word) >= minLength:
            wordsCounted = wordsCounted + 1
            continue
        else:
            continue


    strdelim=convertToString(delimiters)

    words = textInFile.split(" ")
    print(words)
    print(len(words))

    for x in words:
        if len(x) < minLength:
            words.remove(x)


    if strdelim not in textInFile:
        print(strdelim+ " is not in this text file")
    sentences = textInFile.split(strdelim)
    
    if "" in sentences:
        sentences.remove("")

    print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength =  wordsCounted / len(sentences)
    else:
        aveSentenceLength = words

    # Round down to nearest integer
    return math.floor(aveSentenceLength)



def main():
    con = True
    while con:
        userFile = input("Enter the file path to the .txt file you wish to analyze: ")
        try:
            testFile = open(userFile)
            print("Great!")
            con = False
        except:
            print("Error. You may have entered an invalid file path.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces: ")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Enter the minimum length of a word (must be a positive integer): "))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()

    