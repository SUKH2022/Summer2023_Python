# COMP1112 Mid-Term
# Part2_B.py
# Name: Sukhpreet Saini
# Student #:

# The program expects to receive an integer input, don't worry about invalid inputs.
# Depending on the input the program will print:
# "Wowee, that's the old!" if the input is <= 1900
# "That's pretty recent!" if the input is > 1900 but < 2023
# "Crazy! What's it like in the future?" if the input is > 2023

# the yr variable is taking the input from the user and converting it in the int
year = int(input("Hello! What year did you travel from? "))

# it is checking if the yr is < than 1900 or equal to 1900. else  it will predict the yr is the future and print the output in the terminal
if year <= 1900:
    print("Wowee, that's old!")
elif year > 1900 and year < 2023:
    print("That's pretty recent!")
else:
    print("Crazy! What's it like in the future?")

'''
Hello! What year did you travel from? 2020
That's pretty recent!
'''