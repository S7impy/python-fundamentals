'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

pi = 3.14
radius = 3.14
height = 5

volume = pi * (radius ** 2) * height

lateral_surface = 2 * pi * radius * height
top_surface = pi * (radius ** 2)

total_surface= lateral_surface + 2 * top_surface

print(f"The volume of the cylinder is {volume}")
print(f"The surface of the cylinder is {total_surface}")