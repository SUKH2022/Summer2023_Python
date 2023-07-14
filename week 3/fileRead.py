file = open("myTestFile.txt", "r")

# Use for larger files that can be read piecemeal
for line in file:
    print(line)

# User for smaller files or files that must remain as a whole
file.read()

file.close()