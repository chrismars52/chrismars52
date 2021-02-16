#Hello World
print("Hello World!")
print("Aparently, Hello World as the first code printed by new students of a programming language is a tradition that dates back to the 70's.")

#Testing Calculations
print("Here are some calculations I can do")
print(str(10//3) + " is the integer product of 10 divided by three")
print(str(10%3) + " is the remainder of 10 divided by three")

#Testing Functions
def getSeconds(hours, minutes, seconds):
    print("Your input comes to " + str(hours * 3600 + minutes * 60 + seconds) + " seconds.")
getSeconds(1,2,3)
