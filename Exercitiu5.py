def matrice_zero(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i == j:
                matrice[i][j] = 0
    return matrice


if __name__ == '__main__':
    matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrice_zero(matrice))
