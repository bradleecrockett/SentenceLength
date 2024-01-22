import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")
    validWords = len(words)

    for i in words:
        if len(i) < minLength:
            validWords -= 1
    # print(words)

    sentences = textInFile.split(".")
    sentences.remove("")

    # print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = validWords / len(sentences)
    else:
        aveSentenceLength = validWords

    return round(aveSentenceLength, 0)


def main():
    error = True
    userFile = input("Enter the file path to the .txt file you wish to analyze.")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces")
    userDelimeters = userDelimeters.split(" ")
    while error:
        try:
            minLength = int(input("Enter the minimum length of a word (must be a positive integer)"))
            error = False
        except: ValueError
        print("Input must be an integer")
    """ while error:
        minLength = input("Enter the minimum length of a word (must be a positive integer)")
        if (type(minLength) is int):
            if (minLength >= 1):
                error = False
            else:
                print("Invalid integer.")
        else:
            print("Input must be an integer.")
    """

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()
