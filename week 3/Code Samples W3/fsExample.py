import os

# Create a folder
os.mkdir("testFolder")

# Open folder
os.chdir("testFolder")

# Print current directory
print(os.getcwd())

# Create a directory if it doesn't exist
if not os.path.exists("testConditionalCreate"):
    os.mkdir("testConditionalCreate")

# Rename a folder or file
os.rename("testConditionalCreate", "testRename")

# Delete a folder
os.rmdir("testRename")