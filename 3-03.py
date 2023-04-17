import math

for number in range(10,99):
    x = number/7
    if(number % 7 == 0):
        y = number % 10
        if y == x:
            print(number)
