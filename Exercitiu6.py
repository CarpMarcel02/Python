def functie_ciudata(x, *lists):
    dictionar = {}
    result = []
    for lista in lists:
        for item in lista:
            if item in dictionar:
                dictionar[item] += 1
            else:
                dictionar[item] = 1

    for i, count in dictionar.items():
        if x == count:
            result.append(i)
    return result


if __name__ == '__main__':
    lista1 = [1, 2, 2, 3, 3, 4]
    lista2 = [2, 3, 4, 5, 6]
    lista3 = [4, 5, 6, 7, 8, 9]
    print(functie_ciudata(2, lista1, lista2, lista3))
