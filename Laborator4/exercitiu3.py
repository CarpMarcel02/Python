# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization.
# The class should provide methods to access elements (get and set methods)
# and some methematical functions such as transpose, matrix multiplication and a method that allows iterating
# through all elements form a matrix an apply a transformation over them (via a lambda function).


class Matrix:
    def __init__(self, rows, cols):
        self.matrix = []
        self.nr_rows = rows
        self.nr_cols = cols
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.matrix.append(row)

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def get_value(self, row, col):
        return self.matrix[row][col]

    def get_matrix(self):
        return self

    def print_matrix(self):
        for i in range(self.nr_rows):
            for j in range(self.nr_cols):
                print(self.matrix[i][j], end=" ")
            print()

    def transpose_matrix(self):
        matrice_transposata = []
        for j in range(self.nr_cols):
            row = []
            for i in range(self.nr_rows):
                row.append(self.matrix[i][j])
            matrice_transposata.append(row)
        self.matrix = matrice_transposata
        aux = self.nr_cols
        self.nr_cols = self.nr_rows
        self.nr_rows = aux

    def matrix_multiplication(self, matrice):
        if self.nr_rows != matrice.nr_cols:
            print("matricele nu corespund pentru inmultire")
            return None

        matrice_rezultat = Matrix(self.nr_rows, matrice.nr_cols)

        for i in range(self.nr_rows):
            for j in range(matrice.nr_cols):
                sum = 0
                for k in range(self.nr_cols):
                    sum += self.matrix[i][k] * matrice.matrix[k][j]
                matrice_rezultat.matrix[i][j] = sum
        return matrice_rezultat

    def apply_transformation(self, transformation_function):
        for i in range(self.nr_rows):
            for j in range(self.nr_cols):
                self.matrix[i][j] = transformation_function(self.matrix[i][j])


matrix = Matrix(2, 3)
#matrix.print_matrix()
matrix.set_value(0, 0, 1)
matrix.set_value(0, 1, 2)
matrix.set_value(0, 2, 7)
matrix.set_value(1, 1, 5)
matrix.set_value(1, 2, 9)
matrix.print_matrix()
#matrix.transpose_matrix()
print()
matrix1 = Matrix(3, 2)
matrix1.set_value(0, 0, 1)
matrix1.set_value(0, 1, 3)
matrix1.set_value(1, 0, 1)
matrix1.set_value(1, 1, 4)
matrix1.set_value(2, 0, 2)
matrix1.set_value(2, 1, 2)
matrix1.print_matrix()
resultat = matrix.matrix_multiplication(matrix1)
resultat.print_matrix()

print()
resultat.apply_transformation(lambda x: x * 2)
resultat.print_matrix()


print(matrix.get_value(1, 1))
print(matrix)
