#! /usr/bin/env python3

def palindrome(string):

    string = string.lower() #приведем строку к нижнему регистру
    string = string.replace(' ', '') #удалим пробелы
    rev_string = ''.join(reversed(string)) #сделаем реверс строки
    #rev_string = string[::-1]
    return string == rev_string

my_str = input('Input string:')
print('Yes, it`s palindrome' if palindrome(my_str) else 'No, it`s not palindrome')
