# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

"""
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""

def series_sum(n):
    sum = 0
    for i in range (0,n):
        sum += 1/(1+3*i)
    return format((round(sum,2)),'.2f') #metoda "format" vrací string
series_sum(5)