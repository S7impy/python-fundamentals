'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
text = input("Enter a text: ")
text_split = text.split()
result_list = []

for item in text_split:
    result_list.append(tuple(item))


print(result_list)