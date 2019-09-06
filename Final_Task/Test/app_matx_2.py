#!/usr/bin/python
# -*- coding: utf-8 -*-
from matrix_2 import Matrix

def intcheck(a):
    res = True
    try:
        int(a)
    except:
        res = False
    return res

cr_mtrx = input(
    'Чтобы создать произвольные матрицы заданных размеров введите "1"\n'
    'Чтобы создать матрицы со стандартного ввода введите "2"\n'
    'Чтобы записать матрицу в файл и считать матрицу из файла введите "3"\n')

if intcheck(cr_mtrx):
    if int(cr_mtrx) == 1:
        n = int(input('Введите длину матрицы: '))
        m = int(input('Введите высоту матрицы: '))
        
        print("Создадим матрицу M1")
        M1 = Matrix.makeRandom(m, n)
        print(str(M1))
        print("Единичная - " + str(M1.is_identity()))
        print("Квадратная - " + str(M1.is_square()))
        print("Нулевая - " + str(M1.is_zero()))
        print("Диагональная - " + str(M1.is_diagonal()) + "\n")
        
        print("Создадим матрицу M2")
        M2 = Matrix.makeRandom(m, n)
        print(str(M2))
        print("Единичная - " + str(M2.is_identity()))
        print("Квадратная - " + str(M2.is_square()))
        print("Нулевая - " + str(M2.is_zero()))
        print("Диагональная - " + str(M2.is_diagonal()) + "\n")
        
        print("Сложение:\n" + str(M1 + M2))
        print("Вычитание:\n" + str(M1 - M2))
        print("Транспонируем матрицу M2:")
        M2.transpose()
        print(M2)
        print("Умножение:\n" + str(M1 * M2))

    elif int(cr_mtrx) == 2:
        print("Создадим матрицу M1")
        M1 = Matrix.readStdin()
        print(M1)
        print("Единичная - " + str(M1.is_identity()))
        print("Квадратная - " + str(M1.is_square()))
        print("Нулевая - " + str(M1.is_zero()))
        print("Диагональная - " + str(M1.is_diagonal()) + "\n")

        print("Создадим матрицу M2")
        M2 = Matrix.readStdin()
        print(M2)
        print("Единичная - " + str(M2.is_identity()))
        print("Квадратная - " + str(M2.is_square()))
        print("Нулевая - " + str(M2.is_zero()))
        print("Диагональная - " + str(M2.is_diagonal()) + "\n")

        print("Сложение:\n" + str(M1 + M2))
        print("Вычитание:\n" + str(M1 - M2))
        print("Транспонируем матрицу M2:")
        M2.transpose()
        print(M2)
        print("Умножение:\n" + str(M1 * M2))

    elif int(cr_mtrx) == 3:
        path = input('Введите путь к файлу матрицы: ')
        M1 = Matrix.makeRandom(3, 4)
        M1.save(path)
        M2 = Matrix.readGrid(path)
        print ("Сравним записанную и считанную матрицы -", M2 == M1)

    else:
        print ("wrong input, end of program") 

else:
    print ("wrong input, end of program")
