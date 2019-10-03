'''
-------------------------------------------------------------------------------
Name:		problem 2.py
Purpose:	Find how many pieces of chicken will each student and Mr.Fabroa get

Author:	Chan.J

Created:  date in 03/10/2019
------------------------------------------------------------------------------
'''

# obtain the number of students in the class and number of pieces of chicken
student = int(input("Enter the number of students in the class: "))
chicken = int(input("Enter the number of pieces of chicken: "))

# calculate how many pieces each student and Mr. Fabroa would get
pieces = chicken // student
Mr.Fabroa = chicken % student

# output the amount of chicken students and Mr. Fabroa will get
print("Each student will get " + str(pieces))
print("pieces and Mr. Fabroa will get " + str(fabroa) + " pieces.")