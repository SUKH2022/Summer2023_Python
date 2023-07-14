# COMP1112 Mid-Term
# Part1_A.py
# Name: Sukhpreet Saini
# Student #: 200520246

'''
This code creates a range of numbers from 4 to 70, incrementing by 3, and filters the numbers to include only those divisible by 9. 
The filtered numbers are then printed to the terminal window
'''

# it is creating a range of no.s starting from 4 to 70 and it is incrementing by 3.
numList = range(4, 70, 3)

# a  filter functions is used here which is checking if the x variable is divisible by 9 and gives 0 as a result. 

#  Moreover, it is also converting the values in the list ans storing it in the filtlist.

filtList = list(filter(lambda x: x // 9 == 0, numList))

# its is only printing the values in the terminal 
print(filtList)

'''
[4, 7]
'''