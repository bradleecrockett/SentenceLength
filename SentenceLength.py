
directory = input("Where is the file located? ")
delimiter = input("What are the sentence delimiters? ")
minLength = input("What is the minimum length of a word? ")

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
        print(lengths) #delete
        average = 0
        count = 0
        for num in lengths:
            average += num
            count += 1
        print(average) #delete
        print(count) #delete
        average = average/count
        print(average) #delete
        average = round(average)
        print(average) #delete
        return average

    except:
        print("Please enter a valid directory")
        openFile()
    textFile.close();

print(sentenceLength(directory, delimiter, minLength))


