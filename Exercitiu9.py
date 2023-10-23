def spectation(matrice):
    result = set()
    for i in range(1, len(matrice)):
        for j in range(len(matrice[i])):
            for k in range(i):
                if matrice[i][j] <= matrice[k][j]:
                    result.add((i, j))
    return result


if __name__ == '__main__':
    matrice = [[1, 2, 3, 2, 1, 1],
               [2, 4, 4, 3, 7, 2],
               [5, 5, 2, 5, 6, 4],
               [6, 6, 7, 6, 7, 5]]
    print(spectation(matrice))
