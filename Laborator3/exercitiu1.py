# Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def functie(lista1, lista2):
    setul_intersectie = set(lista1)
    setul_intersectie = setul_intersectie.intersection(lista2)

    setul_reunire = set()
    setul_reunire.update(lista1, lista2)

    setul_a_minus_b = set()
    setul_a_minus_b.update(lista1)
    setul_a_minus_b = setul_a_minus_b.difference(lista2)

    setul_b_minus_a = set()
    setul_b_minus_a.update(lista2)
    setul_b_minus_a = setul_b_minus_a.difference(lista1)

    return setul_intersectie, setul_reunire, setul_a_minus_b, setul_b_minus_a


if __name__ == '__main__':
    print(functie([2, 3, 5, 7], [5, 2, 1, 9, 8]))
