import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()


    words = []
    allWords = textInFile.split()
    for word in allWords:
        if len(word) > minLength:
            words.append(word)


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

    return round(aveSentenceLength, 0)


def main():
    userFile = input("Enter the name to the .txt file you wish to analyze: ")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                           "delimiters separated by spaces: ")
    minLength = eval(input("Enter the minimum length of a word (must be a positive integer): "))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()
