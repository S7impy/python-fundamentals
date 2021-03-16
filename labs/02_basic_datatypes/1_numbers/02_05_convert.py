'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

number = 33
float_number = float(number)
print(float_number)

int_float_number = int(float_number)
print(int_float_number)

a = 3.67
b = 8
division_float = number // a
print(division_float)
division_int = number // b
print(division_int)

x = int(input("Enter a number: "))
y = int(input("Enter a new number: "))
print(x * y)

