import os
import sys
from tkinter import Y

file_paths = sys.argv[1:]

def findAverageSentence(filePath, delimiters, minLength):
    try:
        file = open(filePath)
    except:
        print("This file was either invalid or not found. Please restart the program and use a proper file name.")
        exit()
    
    textInFile = file.read()
    words = textInFile.split("  ")
    words = words.split(" ")
    # print(words)

    sentences = textInFile.split(".")
    sentences.remove("")
    print(sentences)

    # print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return round(aveSentenceLength, 0)

def findAverageWord(filePath, delimiters):
    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")
    # print(words)

    sentences = textInFile.split(".")
    sentences.remove("")
    letters = len(textInFile)
    letters = letters - textInFile.count(" ")
    letters = letters - textInFile.count(".")
    if(words == 0):
        averageWordLength = 0
    else:
        averageWordLength = letters/len(words)

    return round(averageWordLength, 2)



def main():
    userFile = input("Enter the file path to the .txt file you wish to analyze. ")
    #checks if userFile is a .txt or not vv 
    if not os.path.isfile(userFile):
        print("File not .txt please enter a new file")
        userFile = input("Enter the file path to the .txt file you wish to analyze. ")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "breaks separated by spaces. ")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Enter the minimum character length of a word (must be a positive integer). "))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))
    print("The average letter per words is:", findAverageWord(userFile, userDelimeters))

    #hi <3

    while True:
        go_again = input("Would you like to enter a new file? y/n: ")
        if go_again == "y":
            if (file_paths):
                userFile = file_paths[0]
            else:
                userFile = input("Enter the file path to the .txt file you wish to analyze.")
            userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                                "breaks separated by spaces")
            userDelimeters = userDelimeters.split(" ")
            minLength = eval(input("Enter the minimum character length of a word (must be a positive integer)"))
            if (minLength < 1):
                minLength = 1

            print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))
        elif go_again == "n":
            break
        else:
            print("Please enter y or n")



if __name__ == "__main__":
    main()
    exit = input("Press enter to stop")
    # try to keep whose ever this addition was
