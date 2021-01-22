import os

def convertToString(delimiter):
    new = ""
    for x in delimiter:
        new += x
    return new

def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()
    strdelim=convertToString(delimiters)

    words = textInFile.split(" ")
    # print(words)

    if strdelim not in textInFile:
        print(strdelim+ " is not in this text file")
    sentences = textInFile.split(strdelim)
    
    if strdelim==".":
        sentences.remove("")

    # print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return round(aveSentenceLength, 0)


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
