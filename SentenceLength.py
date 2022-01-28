import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
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
    userFile = input("Enter the file path to the .txt file you wish to analyze.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces")
    userDelimeters = userDelimeters.split(" ")
    goodLength = False
    minLength = ""
    while goodLength == True:
        minLength = eval(input("Enter the minimum length of a word (must be a positive integer)"))
        try:
            goodLength = True
            if (minLength < 1):
                minLength = 1
        except TypeError:
            print("Please enter a valid input: ")
            goodLength = False
    

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()
