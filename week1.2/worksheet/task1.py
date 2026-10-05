# Worksheet 1.2: Task 1 Solution
# Worksheet 1.2: Task 2 Solution
"""
Edit the file task1.py. In this file, write a program that
• Asks the user to enter an integer grade in the range 0 to 100
• Converts that grade into a result of Distinction, Pass or Fail, where
▫ Fail = 0 – 39
▫ Pass = 40 – 69
▫ Distinction = 70 – 100
• Prints out the numeric grade and the result, in the same format as the examples below:
82 is a Distinction
57 is a Pass
36 is a Fail
If the user enters something that isn't a number, or they enter an integer value outside the required
range, the program should immediately exit, after first displaying this exact error message on the
standard error channel:
Error: Grade must be an integer between 0 and 100
Use the exit() function from Python’s sys module to achieve this. Here is an example of how you
import this module and use the exit() function:
import sys
sys.exit("Error!")
Hint: strings have a method isdecimal() that will tell you whether the string consists of
characters that could represent a decimal integer.

"""
import sys
ps = True
try:
    val = int(input("enter a number that within range 0-100"))
except ValueError:
    ps = False

if ps:
    if val >= 0 and val <= 39:
        print(f"{val} is a Fail")
    elif val >= 40 and val <= 69:
        print(f"{val} is a Pass")
    elif val >= 70 and val <= 100:
        print(f"{val} is a Distinction")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")
    



