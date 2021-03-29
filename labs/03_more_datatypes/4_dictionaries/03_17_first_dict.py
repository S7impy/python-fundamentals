'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
input_string = input("Enter the elements of the list separated with spaces: ")
split_list = input_string.split()
for i in range(0, len(split_list)):
    split_list[i] = int(split_list[i])

dir ={}

for i in split_list:
    dir[i] = i * i

print(dir)