
import math

def circum_of_a_circle(radius):
    _circum = 2 * math.pi * radius
    return _circum

radius = float(input('What is the circles radius? '))


circum = circum_of_a_circle(radius)
print(f'The circum of the circle is {circum}')