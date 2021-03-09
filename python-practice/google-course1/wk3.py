#practising while loops
def attempts(n):
    x = 1
    while x <= n:
        print("Not there yet... x=" + str(x))
        x += 1
    print("Done")

attempts(4)

#Adding Squares
print
print
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum
print(sum_squares(10)) # Should be 285

#Hi to Friends
print
print
friends = ['Josh', 'Eman', 'Anthony', 'Joseph']
for friend in friends:
    print("Sup, " + friend)
print
print
print("Use for loops when you have a sequence you want to iterate")
print("Use while loops when you want to continue until a condition changes")
print("If you can use both, up to you... I prefer For Loops")
print
print
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
        print(result)
    return result
factorial(5)
print
print
product = 1
for i in range(1,10):
    product = product * i
    print(product)
print
print
print("For Range Function...")
print("One parameter will create a sequence, one-by-one, from zero to one less than the parameter.")
print("Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.")
print("Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.")
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))
print
print
print("Dominoes problem")
for i in range (7):
    for j in range (i, 7):
        print("[ " + str(i) + "|" + str(j) + " ]")
print
print ("figuring out factorials")
def factorial(n):
    result = 1
    if n > 0:
        for x in range(1,n):
            result = result * x
    return result

for n in range(10):
    print(n, factorial(n+1))
print
print("first 10 cube numbers")
for x in range(1,11):
  print(x**3)
print
print
print("Recursion is the repeated application of the same procedure to a smaller problem")
print("Recursion lets us tackle complex problems by reducing the problem to a simpler one")
print("Eg. Long line, to find out how many people in front. Ask person in front how many people in front, keeps going until the front of line, then goes back and adds person in front + 1")
print("In program, recursion is a way of doing a repetitive task by having the function call itself... usually with a modified parameter, until it reaches a specific parameter called base case")
print
print
def factorial(n):
    print("Factorial called with " + str(n))
    if n<2: #base case
        print("Base case reached, returning 1")
        return 1
    result = n * factorial(n-1) #recursive case
    print("Returning " +str(result) + " for factorial of " + str(n))
    return result
factorial(100)
print
print
def sum_positive_numbers(n):
    print ("Currently n is = " + str(n))
    # The base case is n being smaller than 1
    if n < 1:
        return 0
    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    result = n + sum_positive_numbers(n-1)
    print("currently, result is = " + str(result))
    return result

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
print
print
#Basic Recursive Structure
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
print
print
print("STUDY MORE ON RECURSIVE STRUCTURES!")
print
print
print("Figure this one out!!")
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#why did you find this so hard to figure out?
print
print
def digits(n):
	count = 0
	if n == 0:
	   count = 1
	while (n>0):
		count += 1
		n = n // 10
	return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
print
print
for x in range(10):
    for y in range(x):
        print("y = " + str(y))
