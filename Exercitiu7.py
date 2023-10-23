def is_palindrom(numar):
    cuvant=str(numar)
    ok = 0
    for i in range(len(cuvant)):
        if (cuvant[i] != cuvant[len(cuvant) - 1 - i]):
            ok = 1

    return ok

def tupla(lista):
    maxi = 0
    counter = 0
    for i in lista:
        if is_palindrom(i) == 0:
            counter += 1
            if i > maxi:
                maxi = i
    return counter, maxi


if __name__ == '__main__':
    print(tupla([11, 24, 353, 25, 19, 4322, 5]))
