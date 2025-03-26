#Author: Alex Hall
#For: CMPSC132 SP25, Assignment 3

class Cars:
    #str _make
    #str _model
    #int _year

    def __init__(self, make, model, year): #constructor
        self._make = make
        self._model = model
        self._year = year

    def setMake(self, m): #setter
        self._make = m

    def setModel(self, m): #setter
        self._model = m

    def setYear(self, y): #setter
        self._year = y

    def getMake(self): #getter
        return self._make

    def getModel(self): #getter
        return self._model

    def getYear(self): #getter
        return self._year

def main():
    print("Hello Cars()!")
    number_of_cars = 3 #int(input("How many cars would you like to enter?"))
    #car_list = ["0"] * number_of_cars

    for i in range(number_of_cars):
        #print("Hello Cars()!")
        #car_list[i] = Cars(Cars.setMake())

        #initialize new Car() with default values
        new_car = Cars("", "", 0)

        new_car.setMake(input("What is the cars Make? "))
        new_car.setModel(input("What is the cars Model? "))
        new_car.setYear(input("What is the cars Year? "))

        #new_car = Cars(input("What is the cars Make? "), input("What is the cars Model? "), input("What is the cars Year? "))

        print("\nYour car is a:")
        print(new_car.getMake(), ", ", new_car.getModel(), ", ", new_car.getYear(), "\n")

    #for _ in number_of_cars:
        #ShowCars

if __name__ == "__main__":
    main()