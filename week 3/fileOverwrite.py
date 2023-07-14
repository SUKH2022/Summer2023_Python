myFile = open("myTestFile.txt", "w")
myFile.write("Madison")
myFile.truncate()
myFile.close()