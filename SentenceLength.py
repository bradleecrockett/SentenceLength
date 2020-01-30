
def averageLen(delimeter, directory, minLength):
    text = open(directory)
    textInFile = text.read()
    words = textInFile.split(" ")
    wordsToRemove = []
    lengths = []
    for i in words:
        if len(i) - 1 < minLength:
            wordsToRemove.append(i)

    for i in wordsToRemove:
        words.remove(i)
    num = 0
    for i in words:
        d = False
        for i2 in delimeter:
            if(i[len(i)-1] == i2):
                d = True
        if(d):
            num += 1
            lengths.append(num)
            num = 0
        else:
            num += 1
    print(lengths)

def main():
    delim = input("Enter delimeters(seperated by spaces): ")
    delim = delim.split()
    path = input("Enter the directory for text file: ")
    len = int(input("Enter the min length for a word: "))

    averageLen(delim,path,len)
main()