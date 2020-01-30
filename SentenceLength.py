
directory = input("Where is the file located? ")

try:
    textFile = open(directory, "r")
    print(textFile.read())

except:
    print("Please enter a valid directory")
    openFile()






































