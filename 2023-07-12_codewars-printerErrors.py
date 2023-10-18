# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    array = []
    for letter in s:
        if ord(letter) not in range(97, 110):
            array.append(letter)
        else:
            pass
    arrayLen = len(array)
    sLen = len(s)
    return (f'{arrayLen}/{sLen}')
printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")