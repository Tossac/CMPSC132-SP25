#Author: Alex Hall
#CMPSC132 SP25
#Participation Practice 4

"""
(1) Fix the problem in the following program, so that we do not need to assign the age of the faculty from the main by calling  E1.age = 37.
And the printInfo call for faculty should print the firstname, lastname and the age of the faculty. Please use reusability. 

(2) Now extend the Employee class and add another child class named staff.
The staff class also has two children: administrative_staff and IT_staff
All three classes have the following attributes and methods:


Additional Member variables specific to the classes are
staff: department_name
administrative_staff: yearly_vacation_days
IT_staff: located_at

Member functions (all the printInfo are redefined in each of the following classes and should print all the attributes that the class can have)
staff: printInfo()
administrative_staff: printInfo()
IT_staff:printInfo ()
"""

class Employee:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


    #print the firstname and lastname
    def printInfo(self):
        print(self.firstname, self.lastname)



class Faculty(Employee):
    def __init__(self, fname, lname, age=0):
        super().__init__(fname, lname)
        self.age=age


    #print the firstname, lastname, and their age
    def printInfo(self):
        super().printInfo()
        print(self.age)



#Now extend the Employee class and add another child class named staff.
#The staff class also has two children: administrative_staff and IT_staff

#staff: department_name
class Staff(Employee):
    def __init__(self, fname, lname, department_name):
        super().__init__(fname, lname)
        self.department_name=department_name


    #print the firstname, lastname, and the name of their assigned department
    def printInfo(self):
        super().printInfo()
        print(self.department_name)


#administrative_staff: yearly_vacation_days
class administrative_staff(Staff):
    def __init__(self, fname, lname, department_name, yearly_vacation_days):
        super().__init__(fname, lname, department_name)
        self.yearly_vacation_days=yearly_vacation_days


    #print the firstname, lastname, department, and number of yearly vacation days
    def printInfo(self):
        super().printInfo()
        print(self.yearly_vacation_days)


#IT_staff: located_at
class IT_staff(Staff):
    def __init__(self, fname, lname, department_name, located_at):
        super().__init__(fname, lname, department_name)
        self.located_at=located_at
    

    #print the firstname, lastname, department, and the employees physical location (a large number of them work remotely)
    def printInfo(self):
        super().printInfo()
        print(self.located_at)



if __name__=='__main__':
    E1 = Faculty("Tony", "Stark", 37)
    E1.printInfo()
    print()
    staff1 = Staff("Stephanie", "Francois", "Foreign Language")
    staff1.printInfo()
    print()
    admin1 = administrative_staff("Adam", "Smith", "Economics", 23)
    admin1.printInfo()
    print()
    IT1 = IT_staff("Ian", "Thomas", "Cybersecurity", "Hazelton")
    IT1.printInfo()




