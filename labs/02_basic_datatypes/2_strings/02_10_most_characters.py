'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
first = input("Enter your text here: ")
second = input("Enter your text here: ")
third = input("Enter your text here: ")

print(str(len(first)) + ",", first)
print(str(len(second)) + ",", second)
print(str(len(third)) + ",", third)

if (len(first) > len(second)) and (len(first) > len(third)):
    largest = first
elif (len(second) > len(first)) and (len(second) > len(third)):
    largest = second
else:
    largest = third

print(largest)