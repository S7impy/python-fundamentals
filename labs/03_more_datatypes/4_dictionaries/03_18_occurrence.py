'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_input = input("Enter your text here: ")
result = {}

for i in user_input:
    keys = result.keys()
    if i in keys:
        result[i] += 1
    else:
        result[i] = 1

print(result)