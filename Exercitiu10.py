def functie_ciudata( *lists):
    maxi = max(len(lista) for lista in lists)
    result = []
    for i in range(maxi):
        tuple_elements = []
        for lista in lists:
            if i < len(lista):
                tuple_elements.append(lista[i])
            else:
                tuple_elements.append(None)
        result.append(tuple(tuple_elements))

    return result


if __name__ == '__main__':
    print(functie_ciudata([1,2,3], [5,6,7], ["a", "b", "c"]))



