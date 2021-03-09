#Hello World
print("Hello World!")
print("Aparently, Hello World as the first code printed by new students of a programming language is a tradition that dates back to the 70's.")

#Testing Calculations & trying out the str() function
print
print
print("Here are some calculations I can do")
print(str(10//3) + " is the integer product of 10 divided by three")
print(str(10%3) + " is the remainder of 10 divided by three")

#Testing Functions
print
print
def getSeconds(hours, minutes, seconds):
    print("Your input comes to " + str(hours * 3600 + minutes * 60 + seconds) + " seconds.")
getSeconds(1,2,3)

#Using the Type function
print
print
print(type(getSeconds))

#Trying to return values
print
print
def triangleArea(base, height):
    return base*height/2

areaOne = triangleArea(5,4)
areaTwo = triangleArea(7,3)
sum = areaOne + areaTwo

print("The sum of the two triangles are: " +str(sum))

#Returning multiple values
print
print
def convertSeconds(sec):
    hours = sec//3600
    minutes = (sec - hours * 3600) // 60
    seconds = sec - hours*3600 - minutes *60
    return hours, minutes, seconds

hours, minutes, seconds = convertSeconds(5000)
print(hours, minutes, seconds)

#Consolidating into Functions
print
print
def daysOfMonth(month, days):
    print(month+" has "+str(days)+" days.")

daysOfMonth("July", 31)
daysOfMonth("February", 28)

#Style of code
print
print
print("1. Self Documenting. Should be reflected in names of variables, functions, etc.")
print("-- Refactoring is rewriting code to make it more self-documenting")
print("2. Use comments with #")

#Operators
print
print
print("Branching - The ability of a program to alter its execution sequence.")
def hint_username(username):
    if len(username) < 3:
        print(username + " is invalid. Your username must be a minimum of 3 characters")
    elif len(username) > 15:
        print(username + " is invalid. Your username must be a maximum of 15 characters")
    else:
        print(username + " is valid")
hint_username("chris")
hint_username("la")
hint_username("0123456789012345")
print
print
print("% is called modulo operator - returns remainder")
import random
def is_number_even(num):
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is not even")
for i in range (25):
    is_number_even(random.randint(1,101))
print
def sum(x, y):
		return(x+y)
print(((10 >= 5*2) and (10 <= 5*2)))
