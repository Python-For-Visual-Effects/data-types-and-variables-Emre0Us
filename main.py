"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)
# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number_A= 64
number_B= 32
print(number_A+number_B)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
first_name= "Emre"
last_name= "Us"
Age= "35"
print("hello my name is"+" "+ first_name+ " " + last_name +","+" "+ Age+".")

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."

babysteps= "This is my first Python program."
print( len (babysteps))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
value1= 2112
value2= 1188

print("The 10% overscan of 1920 is" +" "+ str(value1) + " ,and the 1080 is" +" "+ str(value2) +"." )