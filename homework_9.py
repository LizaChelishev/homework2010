def add(x = 0, y = 0):
    sum = x + y
    return sum

def sub(x, y):
    diff = x- y
    return diff

def mul(x, y):
    pro = x * y
    return pro

def div(x, y):
    quotient = (x // y) + (x % y)
    return quotient

x = float(int(input('Enter first  number: ')))
y = float(int(input('Enter second  number: ')))
print('The sum of your two numbers is ' + str(add(x, y)))
print('The difference between your two numbers is ' + str(sub(x, y)))
print('The product of your two numbers is ' + str(mul(x, y)))
print('The quotient of your two numbers is ' + str(div(x, y)))