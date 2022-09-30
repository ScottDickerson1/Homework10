
#Wire a class that represents a payroll deduction
#transaction. Each instance should have the
#description, date, charge amount, and employee ID
#as attributes. The class's __init__ method should
#accept an argument for each attribute. The class
#should have accessor methods for each attribute.
#All attributes should be hidden

class deduction:
    def __init__(self,desc,date,amt,id_num):
        self.__desc = desc
        self.__date = date
        self.__amt = amt
        self.__id_num = id_num

    def get_desc(self):
        return self.__desc
    def get_date(self):
        return self.__date
    def get_amt(self):
        return self.__amt
    def get_id_num(self):
        return self.__id_num

