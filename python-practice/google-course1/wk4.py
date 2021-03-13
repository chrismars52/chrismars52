def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
print()
print()
#
#
#
myString = "Never Odd or Even"
newString = ""
reverseString = ""
for i in myString:
    newString += i
    reverseString = i + reverseString
print(newString)
print(reverseString)

#def is_palindrome(input_string):
	# We'll create two strings, to compare them
	#new_string = ""
	#reverse_string = ""
	# Traverse through each letter of the input string

		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		#if input_string[i] != " ":
		#	new_string = "#".join(input_string[i])
		#	reverse_string = ___
	# Compare the strings
	#if ___:
	#	return True
	#return False

#print(is_palindrome("Never Odd or Even")) # Should be True
#print(is_palindrome("abc")) # Should be False
#print(is_palindrome("kayak")) # Should be True
print()
print()

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = sentence.rfind(old)
        new_sentence = sentence[0:i] + new
        return new_sentence
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in Macy"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

print()
print()
def skip_elements(elements):
    new_elements = []
    for index, element in enumerate(elements):
        if index%2 == 0:
            print(str(index) + " " + element)
            new_elements.append(element)
            print(new_elements)
    return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

print()
print()
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
for index, each_file in enumerate(filenames):
    if each_file.endswith(".hpp"):
        print(filenames[index])
        print(each_file[:each_file.find(".hpp")+2])

print()
print()
def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    new_words = []
    for word in words:
        # Create the pig latin word and add it to the list
        new_word = word[1:len(word)] + word[0] + "ay"
        new_words.append(new_word)
        # Turn the list back into a phrase
    return ' '.join([word for word in new_words])

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

print()
print()
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for index in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if index >= value:
                result += letter
                index -= value
            else:
                result += "-"
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

print("------------------------")
print("========================")
def group_list(group, users):
    members = "{}: {}".format(group,', '.join([user for user in users]))
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

print("------------------------")
print("========================")
def guest_list(guests):
    for name, age, job in guests:
        print("{} is {} years old and works as {}".format(name, str(age), job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

print("------------------------")
print("========================")
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothe in wardrobe.keys():
    for colour in wardrobe[clothe]:
        print(colour)

print("------------------------")
print("========================")
#def groups_per_user(group_dictionary):
group_dictionary = {"local": ["admin", "userA"],"public":  ["admin", "userB"],"administrator": ["admin"]}
user_groups = {}
for groups in group_dictionary.keys():
    for user in group_dictionary[groups]:
        if user in user_groups:
            user_groups[user].append(groups)
        else:
            user_groups[user] = [groups]

print(user_groups)

print("------------------------")
print("========================")

def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    print(guests1)
    print(guests2)
    for name in guests2.keys():
        if name not in guests1:
            guests1.update({name:guests2[name]})
    return guests1

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

print("------------------------")
print("========================")

def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text.lower():

        if type(letter) == str and letter != " ":
            if letter in result:
                result[letter] += 1
            else:
                result.update({letter:1})
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

print("------------------------")
print("========================")

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
