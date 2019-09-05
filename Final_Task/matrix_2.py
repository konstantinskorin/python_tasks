import random
import operator
import sys


class MatrixError(Exception):
    """ Исключение для класса Matrix """
    pass

class Matrix(object):
    
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
        
    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return rep
            
    def is_identity(self):
        """ Проверка является ли матрица единичной
        (диагональные элементы которой равны 1) """

        if self.m != self.n:
            return False
        for r in range(self.m):
            for c in range(self.n):
                if (c == r and self.rows[r][c] != 1) or (c != r and self.rows[r][c] != 0):
                    return False
        return True

    def is_square(self):
        """ Проверка является ли матрица квадратной """
    
        res = False
        if self.m == self.n:
            res = True
        return res

    def is_zero(self):
        """ Проверка является ли матрица нулевой
        (все её элементы равны нулю) """

        res = True
        for row in self.rows:
            for element in row:
                if element != 0:
                    res = False
        return res

    def is_diagonal(self):
        """ Проверка является ли матрица диагональной
        (все ее элементы, стоящие вне главной диагонали, равны 0) """

        if self.m != self.n:
            return False
        for r in range(self.m):
            for c in range(self.n):
                if c != r and self.rows[r][c] != 0:
                    return False
        return True
                     
    def transpose(self):
        """ Транспонирование матрицы (изменяет текущую матрицу) """
        
        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]

    def getTranspose(self):
        """ Возвратить транспонирование матрицы
        без изменения самой матрицы """
        
        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows =  [list(item) for item in zip(*self.rows)]
        
        return mat

    def getRank(self):
        return (self.m, self.n)

    def __eq__(self, mat):
        """ Проверка равенства """

        return (mat.rows == self.rows)
        
    def __add__(self, mat):
        """ Сложение """
        
        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        """ Вычитание """
        
        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [item[0]-item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        """ Умножение """
        
        matm, matn = mat.getRank()
        
        if (self.n != matm):
            raise MatrixError("Matrices cannot be multipled!")
        
        mat_t = mat.getTranspose()
        mulmat = Matrix(self.m, matn)
        
        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], mat_t[y])])

        return mulmat

    def save(self, filename):
        """ Сохранение в файл """
        open(filename, 'w').write(str(self))
        
    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])

        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError("inconsistent row length")
        mat = Matrix(m,n, init=False)
        mat.rows = rows

        return mat
        
    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):
        """ Создание матрицы со случайными элементами """
        
        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    @classmethod
    def makeZero(cls, m, n):
        """ Создание нулевой матрицы """

        rows = [[0]*n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def makeId(cls, m):
        """ Создание единичной матрицы """

        rows = [[0]*m for x in range(m)]
        idx = 0
        
        for row in rows:
            row[idx] = 1
            idx += 1

        return cls.fromList(rows)
    
    @classmethod
    def readStdin(cls):
        """ Создание матрицы со стандартного ввода """
        
        print ('Enter matrix row by row. Type "q" to quit')
        rows = []
        while True:
            line = sys.stdin.readline().strip()
            if line=='q': break

            row = [int(x) for x in line.split()]
            rows.append(row)
            
        return cls._makeMatrix(rows)

    @classmethod
    def readGrid(cls, fname):
        """ Чтение матрицы из файла """

        rows = []
        for line in open(fname).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)

        return cls._makeMatrix(rows)

    @classmethod
    def fromList(cls, listoflists):
        """ Создание матрицы из списка """

        # Пример: Matrix.fromList([[1 2 3], [4,5,6], [7,8,9]])

        rows = listoflists[:]
        return cls._makeMatrix(rows)

class HorizontalVector(Matrix):
    def __init__(self, m, init = True):
        super(HorizontalVector, self).__init__(1, m, init)

class VerticalVector(Matrix):
    def __init__(self, n, init = True):
        super(VerticalVector, self).__init__(n, 1, init)
