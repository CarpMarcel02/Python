def functi_multiple(a, b):
    a_minus_b = list()
    b_minus_a = list()
    a_intersectat_b = list()
    a_reunit_b = set()
    for i in a:
        gasit = 0
        for j in b:
            if i == j:
                gasit = 1
        if gasit == 0:
            a_minus_b.append(i)

    for i in b:
        gasit = 0
        for j in a:
            if i == j:
                gasit = 1
        if gasit == 0:
            b_minus_a.append(i)

    for i in a:
        gasit = 0
        for j in b:
            if i == j:
                gasit = 1
        if gasit == 1:
            a_intersectat_b.append(i)

    for i in a:
        a_reunit_b.add(i)
    for j in b:
        a_reunit_b.add(j)

    return a_minus_b, b_minus_a, a_intersectat_b, a_reunit_b


if __name__ == '__main__':
    lista1 = [11, 42, 51, 512, 23, 15, 7]
    lista2 = [11, 29, 40, 512, 42, 8, 21, 50, 22]
    print(functi_multiple(lista1, lista2))
