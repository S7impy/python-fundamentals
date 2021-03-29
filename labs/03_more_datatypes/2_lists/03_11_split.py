'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

text = input("Enter your text here: ")
items = text.split()
max = 0
maxitem = None

for i in items:
    count = items.count(i)
    if count > max:
        max = count
        maxitem = i

print(maxitem)