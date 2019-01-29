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

    return math.floor(aveSentenceLength)


userFile = input("Enter the file path to the .txt file you wish to analyze.")
userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                       "delimiters separated by spaces")
userDelimeters = userDelimeters.split(" ")

minLength = -1
while not(minLength > 0):
    try:
        minLength = eval(input("Enter the minimum length of a word: "))
    except (NameError, SyntaxError):
        print("That's not a valid number!")

print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))
