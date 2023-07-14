# COMP1112 Mid-Term
# Part3.py
# Name: Sukhpreet Saini
# Student No.: 200520246

'''
It is a func. that takes a string variable and returns a list of index values of which we has capital letter in the str variable
'''
 
def capIndex(str):
    # it is the empty list
    res=[]
    # it is iterating to the length of the str variable
    # if it is in uppercase then it will append the list
    for i in range(len(str)):
        if str[i].isupper():
            res.append(i)
    return res
    # putting the values in the str variable
    str="HeLlO cLaSs"
res= capIndex(str)
print(res)

'''
output is:
[0, 2, 4, 7, 9]
'''