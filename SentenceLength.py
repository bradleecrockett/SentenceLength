print ("this is a test")


























































fileName = input("enter fileName")
file = open(fileName, "r")
for line in file:
    print (line)

file.close()