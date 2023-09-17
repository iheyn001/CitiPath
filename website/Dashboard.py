#Primary page for all profiles
#Has:
# Map view (Base - property insurance, Vault - finances, Equipment - Transportation/Electronics, Potions - Medications/health insurance/overall wellness)
# Equipment should have a way to keep track of your store/manufacturer warranties/electronic insurance
# Medication note: To avoid issues we prompt user to use "codename", have restock reminders (next date of refill) and cost monitors (cost after insurance)
# Side quests
# Progress bar (TBD)

class Base:
    def __init__(self):
        self.__student_housing = False
        self.__apartment = False
        self.__house = False
        self.__renters_insurance = False
        self.__house_insurance = False
        
    def set_initial_status(self, student_housing, apartment, house, renters_insurance, house_insurance):
        self.__student_housing = student_housing
        self.__apartment = apartment
        self.__house = house
        self.__renters_insurance = renters_insurance
        self.__house_insurance = house_insurance
        
    def set_housing(self, student_housing, apartment, house):
        self.__student_housing = student_housing
        self.__apartment = apartment
        self.__house = house
        
    def set_insurance_stat(self, renters_insurance, house_insurance):
        self.__renters_insurance = renters_insurance
        self.__house_insurance = house_insurance
        
class Vault:
    def __init__(self, monthly_pay):
        self.__monthly_pay = monthly_pay
        
class Equipment:
    def __init__(self):
        self.__pc = []
        self.__car = []
        self.__bicycle = []
        self.__motorcycle = []
        
    def add_pc(self, PC):
        self.__pc.append(PC)
        
    def add_car(self, car):
        self.__pc.append(car)
        
    def add_bicycle(self, bicycle):
        self.__pc.append(bicycle)
        
    def add_motorcycle(self, motorcycle):
        self.__pc.append(motorcycle)
        
class Potions:
    def __init__(self):
        self.__potions = []
        
    def add_potion(self, potion):
        self.__potions.append(potion)
        
