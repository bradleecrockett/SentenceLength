


def sentenceLength (directory, delimiters, minLength):
    lengths = []
    try:
        textFile = open(directory, "r")
        text = textFile.read()
        wordCount = 0;
        letterCount = 0;
        for letter in text:
            if(letter == " "):
                if(letterCount >= int(minLength)):
                    wordCount += 1
                    letterCount = 0
            elif(letter == delimiters):
                wordCount += 1
                lengths.append(wordCount)
                wordCount = 0
                letterCount = 0
            else:
                letterCount += 1
        average = 0
        count = 0
        for num in lengths:
            average += num
            count += 1
        average = average/count
        average = round(average)
        return average

    except:
        print("Please enter a valid directory")
        openFile()
    textFile.close();

stillRunning = "y"
while (stillRunning == "y") :
    stillRunning = input("Would you like to see the average word length in a sentence?[y/n]")
    directory = input("Where is the file located? ")
    delimiter = input("What are the sentence delimiters? ")
    minLength = input("What is the minimum length of a word? ")
    print("" + str(sentenceLength(directory, delimiter, minLength)) + (" is the average word length of the given file. "))

