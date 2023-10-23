def group_by_rhyme(lista):
    rhyme_groups = {}

    for cuvant in lista:
        rima = cuvant[-2:]
        if rima in rhyme_groups:
            rhyme_groups[rima].append(cuvant)
        else:
            rhyme_groups[rima] = [cuvant]

    grouped_words = list(rhyme_groups.values())

    return grouped_words


if __name__ == '__main__':
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))