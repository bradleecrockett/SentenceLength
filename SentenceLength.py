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
    userFile = input("Enter the file path to the .txt file you wish to analyze.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Enter the minimum length of a word (must be a positive integer)"))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))
    print("The average letter per words is:", findAverageWord(userFile, userDelimeters))

    #hi <3

if __name__ == "__main__":
    main()
