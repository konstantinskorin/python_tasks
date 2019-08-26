#!/usr/bin/env python


def my_dict(key,value):
  while len(key)>len(value):
    value.append('None') #добавляем значение 'None', если список key больше
  return dict(zip(key, value)) #zip создает объект-итератор, из которого извлекается кортеж, состоящий из двух элементов - первый из списка key, второй из списка value

print(my_dict(['one', 'two', '3', 'Вася'],[1, 2, 3, 4, 5, 6, 7])) #зададим списки


