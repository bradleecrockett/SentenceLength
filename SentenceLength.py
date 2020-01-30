
def averageLen(delimeter, directory, minLength):
    text = open(directory)
    textInFile = text.read()
    words = textInFile.split(" ")

    wordsToRemove = []

    for i in words:
        if len(i) - 1 < minLength:
            wordsToRemove.append(i)

    for i in wordsToRemove:
        words.remove(i)

def main():
    delim = input("Enter delimeter: ")
    path = input("Enter the directory for text file: ")
    len = input("Enter the min length for a word: ")

    averageLen(deli)