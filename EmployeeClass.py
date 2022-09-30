 #EmployeeClass.py - Write a class named Employee that holds the 
 # following data about an employee in attributes: 
 # name, ID number, department, job title and monthly salary.
 # The Employee class’s __init__ method should accept an argument 
 # for each attribute. 
 # The Employee class should have accessor methods for each attribute. 
 # All attribute should be hidden.


class employee:
    def __init__(self,name,id_num,dept,title,salary):
        self.__name = name
        self.__idnum = id_num
        self.__department = dept
        self.__title = title
        self.__salary = salary

    def get_name(self):
        return self.__name
    def get_idn(self):
        return self.__idnum
    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__title
    def get_salary(self):
        return self.__salary

