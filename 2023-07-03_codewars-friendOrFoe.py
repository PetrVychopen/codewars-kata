# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

def friend(x):
    friendlist = []
    for i in x:
        if len(i) == 4:
            friendlist.append(i)
    print(friendlist)
friend(["Ryan", "Kieran", "Jason", "Yous"])