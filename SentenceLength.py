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
    t = input("Enter text file: ")
    d = input("Enter Delimiters: ")
    l = int(input("Enter minimum word length limit: "))
    averageLen(d,t,l)
main()