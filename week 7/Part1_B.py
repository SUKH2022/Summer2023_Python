# COMP1112 Mid-Term
# Part1_B.py
# Name: Sukhpreet Saini
# Student #: 200520246

'''
This code converts the int(grade) into the letter grade. And also asks the user to provide him with a grade's list, then it process it with if-else statements adn show the letter grades for the no. entered in the terminal 

'''

# This is the function which has the parameter named numGrade. This parameter converts to int and store in the grade variable. And it also has conditional statements that checks the values of grade adn returns the grade
def GradeMap(numGrade):
    grade = int(numGrade)
    if grade > 89:
        return "A"
    elif grade > 79:
        return "B"
    elif grade > 69:
        return "C"
    elif grade > 59:
        return "D"
    else:
        return "F"

# it is using a input function  to get the user input and then it is removing the space if there r any with the " " and split`ing it with a comma

# an empty list is also create as the name letterGrade 
grades = input("Enter a list of grades: ").replace(" ", "").split(",")
letterGrades = []

# it is iterating every element in the grades list 
# then the letter is assign to the Grade
for grade in grades:
    letter = GradeMap(grade)
    # it is then printing the grade in the terminal
    print(letter)
    
    """
    Enter a list of grades: 50
    F
    """