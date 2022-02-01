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
    for i in range(5):
        userFile = input("Enter the file path to the .txt file you wish to analyze. ")
        userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces" )
        userDelimeters = userDelimeters.split(" ")
        minLength = eval(input("Enter the minimum length of a word (must be a positive integer): "))
        if (minLength < 1):
            minLength = 1

        print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

        #uses the last average sentence length in order to compare it to your current average sentence length
        int, lastAveSentenceLength = input("Enter the average sentence length of your last essay: ")

        if lastAveSentenceLength > findAverageSentence(userFile, userDelimeters, minLength):
            print("You increased your average sentence length in this text document compare to your last one.")
        elif lastAveSentenceLength == findAverageSentence(userFile, userDelimeters, minLength):
            print("Your average sentence length is equal to that of your last text document.")
        else:
            print("You decreased your average sentence length in this text document compared to your last one.")

        if __name__ == "__main__":
            main()

        another = input("Would you like to check another document? ")
        if another == ("yes", "Yes", "YES"):
            continue
        else:
            break

