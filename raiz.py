from math import sqrt

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

delta = pow(b, 2) - 4 * a * c

if a == 0:
    print('It is not a second degree equation')
elif delta < 0:
    print('It is not a second degree equation')
else:
    print('There are two real roots')
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'the root is: ', x1)
    print(f'The root x2 is: ', x2)
    print('The Delta is: ', delta)