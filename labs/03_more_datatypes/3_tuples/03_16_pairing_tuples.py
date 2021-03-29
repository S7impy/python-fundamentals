'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
input_string = input("Enter the elements of the list separated with spaces: ")
split_list = input_string.split()
split_list.sort(key=int)
last = split_list[-1]
even = split_list[::2]
odd = split_list[1::2]
odd_tuple = (last, 0)
even_range = range(0, len(even))
odd_range = range(0, len(odd))
print(split_list)

if len(even) != len(odd):
    for i in odd_range:
        tuple_pairs = (even[i], odd[i])
        print(tuple_pairs)
    print(odd_tuple)
else:
    for i in even_range:
        tuple_pairs = (even[i], odd[i])
        print(tuple_pairs)


