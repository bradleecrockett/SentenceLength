import os
def spanish():
    userFile2 = input("Ingrese la ruta del archivo .txt que desea analizar.: ")
    userDelimeters = input("Ingresa los caracteres (puntuación) que deseas que sean oración"
                        "delimitadores separados por espacios: ")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Ingrese la longitud mínima de una palabra (debe ser un número entero positivo): "))
    if (minLength < 1):
        minLength = 1

    print("La longitud promedio de la oración es: ", findAverageSentence(userFile2, userDelimeters, minLength))

def english():
    userFile1 = input("Enter the file path to the .txt file you wish to analyze.: ")
    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence "
                        "delimiters separated by spaces: ")
    userDelimeters = userDelimeters.split(" ")
    minLength = eval(input("Enter the minimum length of a word (must be a positive integer): "))
    if (minLength < 1):
        minLength = 1

    print("The average sentence length is: ", findAverageSentence(userFile1, userDelimeters, minLength))


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
    lang  = input("Enter 1 for English or 2 for Spanish: ")
    if lang.lower() == "1":
        english()
    elif lang.lower() == "2":
        spanish()
    
    else:
        main() 

if __name__ == "__main__":
    main()
