class Matrix:
    def __init__(self, m, n, values=()):
        self.m = m
        self.n = n
        if values and not m * n == len(values):
            raise ValueError('matrix size differs from values list')
        self.matrix = [[0]*n for i in range(m)]
        if values:
            for i, v in enumerate(values):
                self.matrix[i//n][i % n] = v

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError('Other matrix have different size!!!')
        values = []
        for r in range(self.m):
            for c in range(self.n):
                values.append(self.matrix[r][c] + other.matrix[r][c])
        return Matrix(self.m, self.n, values)

    def __sub__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError('Other matrix have different size!!!')
        values = []
        for r in range(self.m):
            for c in range(self.n):
                values.append(self.matrix[r][c] - other.matrix[r][c])
        return Matrix(self.m, self.n, values)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError('Other matrix have wrong size!!!')
        values = []
        for c in range(other.m):
            for r in range(self.n):
                s = 0
                for i in range(self.m):
                    s += self.matrix[i][r]*other.matrix[c][i]
                values.append(s)
        return Matrix(other.m, self.n, values)

    def __str__(self):
        string = ''
        for n in range(len(self.matrix[0])):
            for m in range(len(self.matrix)):
                string += str(self.matrix[m][n]) + ' '
            if n + 1 < len(self.matrix[0]):  # ToDo
                string += '\n'
        return string

    def __eq__(self, other):
        if (self.m != other.m) or (self.n != other.n):
            return False
        for c in range(self.m):
            if self.matrix[c] != other.matrix[c]:
                return False
        return True

    def is_identity(self):
        if self.m != self.n:
            return False
        for r in range(self.m):
            for c in range(self.n):
                if (c == r and self.matrix[r][c] != 1) or (c != r and self.matrix[r][c] != 0):
                    return False
        return True

    def is_square(self):
        return self.m == self.n

    def is_zero(self):
        zero = Matrix(self.m, self.n)
        return self.matrix == zero.matrix

    def is_diagonal(self):
        if self.m != self.n:
            return False
        for r in range(self.m):
            for c in range(self.n):
                if c != r and self.matrix[r][c] != 0:
                    return False
        return True

    def transpose(self):
        values = []
        for c in range(self.n):
            for r in range(self.m):
                values.append(self.matrix[r][c])
        return Matrix(self.n, self.m, values)


class HorizontalVector(Matrix):
    def __init__(self, m, values=()):
        super(HorizontalVector, self).__init__(m, 1, values)


class VerticalVector(Matrix):
    def __init__(self, n, values=()):
        super(VerticalVector, self).__init__(1, n, values)


if __name__ == '__main__':
    mat = Matrix(4, 3, (-1, 5, -8, 2, 4, 11, -3, -2, -10, 0, 1, -5))
    mat2 = Matrix(2, 4, (-9, 6, 7, 12, 3, 20, 0, -4))
    mat3 = mat * mat2
    print(mat3)


