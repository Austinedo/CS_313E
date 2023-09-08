"""
  File: spiral.py
  Description: This program simulates an employee system where
              everyone is an employee but there are different
              types of employees that are demonstrated in the
              system by inheriting from the base employee class
              and adding futher functionality to the child class

  Student Name: Austine Do
  Student UT EID: ahd589

  Partner Name: Ahyeon Ko
  Partner UT EID: ak42464

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 9/7/23
  Date Last Modified: 9/13/23
"""

class Employee:
    """
    class Employee that is the base class for all employees
    """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.identifier = kwargs.get('identifier')
        self.__salary = kwargs.get('salary', None)

    @property
    def salary(self):
        """
        Returns the salary of the employee
        """
        return self.__salary

    def __str__(self):
        return f'Employee\n{self.name}, {self.identifier}, {self.__salary}'


############################################################
############################################################
############################################################


class PermanentEmployee(Employee):
    """
    class PermanentEmployee that inherits from class Employee
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits', [])

    def cal_salary(self):
        """
        Calculates salary based on benefits status of permanent employeee
        """
        if self.benefits == ['health_insurance']:
            return self.salary * 0.9
        if self.benefits == ['retirement']:
            return self.salary * 0.8
        return self.salary * 0.7

    def __str__(self):
        return f'PermanentEmployee\n{self.name}, {self.identifier}, {self.salary}, {self.benefits}'


############################################################
############################################################
############################################################


class Manager(Employee):
    """
    class Manager that inherits from class Employee
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus')

    def cal_salary(self):
        """
        Calculates the salary for the Manager class
        """
        return self.salary + self.bonus

    def __str__(self):
        return f'Manager\n{self.name}, {self.identifier}, {self.salary}, {self.bonus}'


############################################################
############################################################
############################################################


class TemporaryEmployee(Employee):
    """
    class TemporaryEmployee that inherit from class Employeee
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours')

    def cal_salary(self):
        """
        Calculates the salary for TemporaryEmployee class
        """
        return self.salary * self.hours

    def __str__(self):
        return f'TemporaryEmployee\n{self.name}, {self.identifier}, {self.salary}, {self.hours}'


############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    """
    class Consultant that inherits from class TemporaryEmployee (level 2 inheritance)
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel')

    def cal_salary(self):
        """
        Calculates the salary for Consultant class
        """
        return float(super().cal_salary()) + float(self.travel * 1000)

    def __str__(self):
        return (f'Consultant\n'
                f'{self.name}, {self.identifier}, {self.salary}, '
                f'{self.hours}, {self.travel}')


############################################################
############################################################
############################################################


class ConsultantManager(Manager, Consultant):
    """
    class Consultant Manager that inherits from class Manager and
    class Consultant (multiple-inheritance)
    """
    def cal_salary(self):
        """
        Calculates the salary for the ConsultantManager class
        """
        return (self.salary * self.hours) + (self.travel * 1000) + self.bonus

    def __str__(self):
        return (f'ConsultantManager\n{self.name}, {self.identifier}, '
                f'{self.salary}, {self.hours}, {self.travel}, {self.bonus}')


############################################################
############################################################
############################################################


###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes.
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
