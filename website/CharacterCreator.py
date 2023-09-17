#Page after account has been created
#Pick a character class (Student, Citizen)
#Set name, age (relevant for health insurance), birthday, gender (M/W/NB)

class Character:
    def __init__(self, name, age, DOB, gender):
        self.__name = name
        self.__age = age
        self.__DOB = DOB
        self.__gender = gender

#Web page interface with appropriate fields