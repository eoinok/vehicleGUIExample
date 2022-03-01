class Vehicle():
    def __init__(self,arg1,arg2,arg3,arg4):
        self.__regNum=arg1
        self.__make=arg2
        self.__model=arg3
        self.__cO2_emissions = arg4

    def get_cO2_emissions(self):
        return self.__cO2_emissions

    def get_annual_tax(self):
        tax = 200
        if (self.__cO2_emissions <= 90):
            tax = 150
        return tax

    def __str__(self):
        return self.__regNum + " " + self.__make + " " + self.__model
