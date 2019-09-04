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
    
    def reset(self):
        """ Reset the matrix data """
        self.rows = [[] for x in range(self.m)]
        
    def is_identity(self):
        if self.m != self.n:
            return False
        for r in range(self.m):
            for c in range(self.n):
                if (c == r and self.rows[r][c] != 1) or (c != r and self.rows[r][c] != 0):
                    return False
        return True

    def is_square(self):
        res = False
        if self.m == self.n:
            res = True
        return res

    def is_zero(self):
        res = True
        for row in self.rows:
            for element in row:
                if element != 0:
                    res = False
        return res

    def is_diagonal(self):
        if self.m != self.n:
            return False
        for r in range(self.m):
            for c in range(self.n):
                if c != r and self.rows[r][c] != 0:
                    return False
        return True
                     
    def transpose(self):
        """ Transpose the matrix. Changes the current matrix """
        
        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]

    def getTranspose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """
        
        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows =  [list(item) for item in zip(*self.rows)]
        
        return mat

    def getRank(self):
        return (self.m, self.n)

    def __eq__(self, mat):
        """ Test equality """

        return (mat.rows == self.rows)
        
    def __add__(self, mat):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        """ Subtract a matrix from this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)
        
        for x in range(self.m):
            row = [item[0]-item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        """ Multiple a matrix with this matrix and
        return the new matrix. Doesn't modify
        the current matrix """
        
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
        open(filename, 'w').write(str(self))
        
    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError("inconsistent row length")
        mat = Matrix(m,n, init=False)
        mat.rows = rows

        return mat
        
    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):
        """ Make a random matrix with elements in range (low-high) """
        
        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    @classmethod
    def makeZero(cls, m, n):
        """ Make a zero-matrix of rank (mxn) """

        rows = [[0]*n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def makeId(cls, m):
        """ Make identity matrix of rank (mxm) """

        rows = [[0]*m for x in range(m)]
        idx = 0
        
        for row in rows:
            row[idx] = 1
            idx += 1

        return cls.fromList(rows)
    
    @classmethod
    def readStdin(cls):
        """ Read a matrix from standard input """
        
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
        """ Read a matrix from a file """

        rows = []
        for line in open(fname).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)

        return cls._makeMatrix(rows)

    @classmethod
    def fromList(cls, listoflists):
        """ Create a matrix by directly passing a list
        of lists """

        # E.g: Matrix.fromList([[1 2 3], [4,5,6], [7,8,9]])

        rows = listoflists[:]
        return cls._makeMatrix(rows)

class HorizontalVector(Matrix):
    def __init__(self, m, init=True):
        super(HorizontalVector, self).__init__(m, 1, init)
