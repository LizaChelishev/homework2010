def min_number(x, y, z):
    min = 0
    if x < y and x < z:
        min = x
    if y < z and y < x:
        min = y
    if z < y and z < x:
        min = z
    return min

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))
print('The minimum number is ' + str(min_number(x, y, z)))