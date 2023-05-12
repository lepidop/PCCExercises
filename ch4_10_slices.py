# from 4_9
cubes =[value**3 for value in range(1,11)]
print("The first 10 cubes are:")
for cube in cubes:
    print(cube)

# first three items
print("The first three cubes are:")
for cube in cubes[0:3]:
    print(cube)

# middle three items
print("The 4th, 5th, and 6th cubes are:")
for cube in cubes[3:6]:
    print(cube)

# last three items
print("The last three cubes are:")
for cube in cubes[-3:]:
    print(cube)