'''
-------------------------------------------------------------------------------
Name:		problem 1.py
Purpose:	Find the temperature in fahrenheit from celsius for Jeremy.

Author:	Chan.J

Created:   date in 3/10/2019
------------------------------------------------------------------------------
'''

# obtain temperature in celsius from user
celsius = float(input("Enter the temperature in celsius: "))

# calculate the fahrenheit from celsius
fahrenheit = celsius*(9/5) + 32

# output the temperature in fahrenheit
print("The temperature in fahrenheit is " + str(fahrenheit))