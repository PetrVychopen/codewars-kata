# https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python

def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

quadrant(1, 2)
quadrant(3, 5)
quadrant(-10, 100)
quadrant(-1, -9)
quadrant(19, -56)