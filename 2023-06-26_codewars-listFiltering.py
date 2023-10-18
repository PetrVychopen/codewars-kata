# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

# Třída - animal, person, integer - obálka, která může mít nějaké metody
# Instance - reálné, už existující objekt vytvořený z třídy (např. Třída - Člověk, Instance - Petr Vychopeň)

def filter_list(l):
    return list(
        filter(lambda item: isinstance(item, int), l)
        )
filter_list([1,2,"dsd","2",3,"fff"])

"""
def filter_list(l):
    print([x for x in l if type(x) is int])
filter_list([1,2,"dsd","2",3,"fff"])
"""