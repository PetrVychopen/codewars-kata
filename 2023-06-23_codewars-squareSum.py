# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

def square_sum(numbers):
    sumo = 0
    for x in numbers:
        sumo += x ** 2
    return sumo
square_sum([0, 3, 4, 5])