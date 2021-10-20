

def get_in_range (min, max):
    while True:
        x = int(input('Enter a number: '))
        if x < min or x > max:
            continue
        else:
            print(f'Your number {x} is leagal')
min = int(input('Enter your minimum number: '))
max = int(input('Enter your maximum number: '))
get_in_range(min, max)