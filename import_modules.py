import math
#area of rhombus has different formulas :
# formula1: Area = sight * height
def rhombus_area(side ,height):
    area = side * height
    return area


side = float(input("Enter side of rhombus :"))
height = float(input("Enter height of rhombus :"))
area = rhombus_area(side,height)
print(f'{area} cm sq.')

#formula2 =: area = (diagonal1 * diagonal2 )/2
def rhombus_area_diagonals(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area


diagonal1 = float(input("Enter Diagonal one :"))
diagonal2 = float(input("Enter Diagonal two :"))

area = rhombus_area_diagonals(diagonal1,diagonal2)
print(f'{area} cm sq.')


import random
def generate_random_number(n):
    numbers = random.randint(0,n)
    if n < 0 :
        print("Value Error")
    return numbers

n = int(input("Enter the upper limit of integers :"))
random_numbers = generate_random_number(n)
print(random_numbers)