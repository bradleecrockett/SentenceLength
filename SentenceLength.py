
import os
import re


def findAverageSentence(filePath, delimiters, minLength):

    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")

    for word in words:
        if (len(word) < minLength):
            words.remove(word)
    # print(words)
    
    
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

    return round(aveSentenceLength, 0)


def main():

    userFile = input("Enter the file path to the .txt file you wish to analyze.")

    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces")

    minLength = eval(input("Enter the minimum length of a word (must be a positive integer)"))

    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))


if __name__ == '__main__':
    main()
