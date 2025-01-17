import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")
    # print(words)

    sentences = textInFile.split(".")
    delimiters = delimiters.split()
    for i in range(len(delimiters)):
        delimiter = delimiters[i]
        if len(delimiters) > 0:
            for j in range(len(sentences)):
                if delimiter in sentences[j]:
                    additionalSentences = (sentences[j].split(str(delimiter)))
                    for sentence in additionalSentences:
                        sentences.append(sentence)
                    sentences.remove(sentences[j])
    sentences.remove("")

    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return int(round(aveSentenceLength, 0))


def main():
    userFile = input("Enter the file path to the .txt file you wish to analyze.\n")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence delimiters separated by spaces.\n")
    minLength = input("Enter the minimum length of a word (must be a positive integer).\n")
    
    minLenPro = ""

    for i in range(len(minLength)):
        # print("1234567890".contains(minLength[i]))
        if (minLength[i] in "1234567890") == False:
            minLenPro = minLenPro + ""
        else:
            minLenPro = minLenPro + minLength[i] 

    print(minLenPro)

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()
