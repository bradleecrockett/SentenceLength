import re
import os
import math


def findAverageSentence(filePath, delimiters, minLength):

    file = open(filePath)
    textInFile = file.read()
    words = textInFile.split(" ")

    wordsToRemove = []
    for i in words:
        if(i.find(".") == -1):
            if (len(i) < minLength):
                wordsToRemove.append(i)
        else:
            if(len(i) - 1 < minLength):
                wordsToRemove.append(i)
    for i in wordsToRemove:
        words.remove(i)
    
    
    # Using regex for delimiters
    delimiters = '[{0}]'.format(delimiters.replace(" ", ""))
    sentences = re.split(delimiters, textInFile)

    
    # Remove empty strings from the sentences list
    while '' in sentences:
        sentences.remove('')

        
    # Remove extra whitespace from beginning and end of each sentence
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
        


    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return math.floor(aveSentenceLength)



def main():
    userFile = input("Enter the file path to the .txt file you wish to analyze.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                        "delimiters separated by spaces")


    minLength = -1
    while not(minLength > 0):
        try:
            minLength = eval(input("Enter the minimum length of a word: "))
        except (NameError, SyntaxError):
            print("That's not a valid number!")
    
    print("Average length of the word: ", findAverageSentence(userFile, userDelimeters, minLength))


main()
