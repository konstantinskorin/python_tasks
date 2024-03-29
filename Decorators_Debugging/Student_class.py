# -*- coding: utf-8 -*-
from datetime import datetime


class Student(object):
    def __init__(
        self, name, surname, birthdate, gender,
            assessment, speciality, coursenumber):

        self.setname(name)
        self.setsurname(surname)
        self.setbirthdate(birthdate)
        self.setgender(gender)
        self.assessment = assessment
        self.speciality = speciality
        self.coursenumber = coursenumber
    
    #скроем атрибуты и зададим доступы ro и rw, используя свойства
    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def gender(self):
        return self.__gender

    @property
    def assessment(self):
        return self.__assessment

    @assessment.setter
    def assessment(self, value):
        self.setassessment(value)

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, value):
        self.setspeciality(value)

    @property
    def coursenumber(self):
        return self.__coursenumber

    @coursenumber.setter
    def coursenumber(self, value):
        self.setcoursenumber(value)

    '''
    установим параметры и необходимые проверки согласно заданию;
    isinstance - проверяем является ли указанный объект экземпляром указанного класса;
    raise - возбуждает указанное исключение
    '''
    def setname(self, value):
        if isinstance(value, str):
            if len(value) <= 25:
                self.__name = value
            else:
                raise ValueError("Name invalid string length")
        else:
            raise ValueError("Name input error")

    def setsurname(self, value):
        if isinstance(value, str):
            if len(value) <= 50:
                self.__surname = value
            else:
                raise ValueError("Surname invalid string length")
        else:
            raise ValueError("Surname input error")

    def setbirthdate(self, value):
        valid = True
        if len(value) != 10:
            valid = False
        else:
            try:
                datetime.strptime(value, '%d.%m.%Y')
            except:
                valid = False
        if valid:
            self.__birthdate = value
        else:
            raise ValueError("Birth date input error")

    def setgender(self, value):
        if (value == 'Male') | (value == 'Female'):
            self.__gender = value
        else:
            raise ValueError("Gender input error")

    def setassessment(self, value):
        if isinstance(value, int):
            if value in range(1, 10):
                self.__assessment = value
            else:
                raise ValueError("Grade invalid value")
        else:
            raise ValueError("Grade input error")

    def setspeciality(self, value):
        if isinstance(value, str):
            if len(value) <= 50:
                self.__speciality = value
            else:
                raise ValueError("Specialty invalid string length")
        else:
            raise ValueError("Specialty input error")

    def setcoursenumber(self, value):
        if isinstance(value, int):
            if value in range(1, 6):
                self.__coursenumber = value
            else:
                raise ValueError("Course invalid value")
        else:
            raise ValueError("Course number input error")

    def __str__(self):
        res = (
            '|' +  "Student: {} {}" + ' | ' + "Birth Date: {}" + ' | ' + "Gender: {}" +
            ' | ' + "Assessment: {}" + ' | ' + "Specialty: {}" + ' | ' +
            "Course number: {}" + '|\n').format(self.name, self.surname, self.birthdate, 
            self.gender, str(self.assessment), self.speciality, str(self.coursenumber))
        return res


    @staticmethod
    def defSt(string):
        args = string.split(':') # разбивает строку на части, используя разделитель ':'
        if args[3] == 'M':
            args[3] = 'Male'
        else:
            args[3] = 'Female'
        args[4] = int(args[4])
        args[6] = int(args[6])
        return Student(
            args[0], args[1], args[2], args[3], args[4], args[5], args[6])


st1 = Student("Konstantin" , "Skorin", "30.09.1986", "Male", 4, "Devops", 5)
print (st1)

st2 = Student.defSt("Ivan:Petrov:01.08.1991:M:8:Java:2")
print (st2)
