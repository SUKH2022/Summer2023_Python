# Get file names from the user
fileName1 = input("What file would you like to select?")
fileName2 = input("What file would you like to compare?")

# Load the requested files
file1 = open(fileName1, "r")
file2 = open(fileName2, "r")

file1Text = file1.read()
file1Lines = file1Text.split("\n")
file2Text = file2.read()
file2Lines = file1Text.split("\n")

# Loop over lines
success = True
failingLines = ""
# range(len(file1Lines)) = [0, 1, 2, ..., 113]
for index in range(len(file1Lines)):
    if file1Lines[index] != file2Lines[index]:
        success = False
        failingLines = file1Lines[index] + "\n" + file2Lines[index]
        break

# Inform user of results
if success:
    print("Yes, the files are the same")
else:
    print("No, the files differ", failingLines)