"""
week2_ex.py
Example code from lecture 2 of COMP1112-02-S23

Developer: Sukhpreet Saini
Date: May 15, 2023
"""
# OR Logical operator
# A or B
# If a OR b is true, the whole statement is true
True or False # = True
False or True # = True
False or False # = False
True or True # = True

# AND Logical operator
# A and B
# If both a and b are true, the whole statement is true
True and False # = False
False and True # = False
False and False # = False
True and True # = True
1 == 1 and 1 == 1

not (1 == 1) # = False

"Hello" == "Hello"

if (1 != 2):
    print("Wow!")

# Example code (does not work)
#res = webClient.GET("www.google.com")
#if (res == 404 or res == 405):
#    print("The website could not be accessed!")

#if (res != 404 and res != 405):
#    print("Connection success")

#if not (res == 200):
#    print("Error accessing website")

z = True
t = False

# Range function is exclusive, here it counts up to but not including 8
x = range(8) # [0, 1, 2, 3, 4, 5, 6, 7]

# Two arguments makes the range function count from one number, up to but not including another
y = range(6, 12) # [6, 7, 8, 9, 10, 11]

for count in range(6):
    print(count)

for letter in "Hello World":
    print(letter, end="/")
    print("Hello")
print("One Time")

while True:
    # Make web requests
    res = webClient.GET("www.google.com")

    if(res == 200):
        break

# Equivalent Statements
#theSum = theSum + count
#theSum += count

theSum = 0
count = 1
while True:
    theSum += count
    # Blah blah

    count += 1
    if count <= 100:
        break
