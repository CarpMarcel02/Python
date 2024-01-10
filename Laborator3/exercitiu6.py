# Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list,
# and b representing the number of duplicate elements in the list (use sets to achieve this objective).

def function(lista):
    elemente_unice = 0
    elemente_duplicate = 0
    dictionar = {}
    for element in lista:
        if element in dictionar:
            dictionar[element] += 1
        else:
            dictionar[element] = 1
    for key, value in dictionar.items():
        if value == 1:
            elemente_unice += 1
        else:
            elemente_duplicate += 1
    print(dictionar)
    return elemente_unice, elemente_duplicate


if __name__ == '__main__':
    print(function([1, 2, 3, 5, 7, 2, 1, 0, 10, 3, 3, 5]))

