"""Conditionals: 
     1. if
     2. elif
     3. else
"""

a = 3

if a == 0:
    print("Number is zero")
elif a > 0:
    print("Number is a positive value")
    if a == 3:
        print("Number is exactly your lucky number")

else:
    print("Number is a negative value")
