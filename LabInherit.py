class car: #base classs
    def __init__(self, a, b, c, d):
        self.make = a
        self.model= b
        self.color = c
        self.year = d

    def display(self):
        print(self.color, self.make,self.model, self.year)

class Sedan(car): #derived class
    #def __init__(self, make,model, color, year, auto_or_manual):
        #super().__init__(make,model,color,year)
        #can also use the Superclass name explicitly like this:
        #might be a worse idea as if the name of the class changes, your code will break
        #car.__init__(make,model,color,year)
        #self.AM=auto_or_manual

    #def setAM(self, trans):
        #super().__init__(make,model,color,year)
        #self.AM = trans

    def display(self):
        super().display()
        print(self.AM)

class SUV(car): #derived class
    def __init__(self, make,model,color, year,underwater):
        super().__init__(make,model,color,year)
        self.UW = underwater
    def display(self):
        super().display()
        print(self.UW)

#class test():
    # def __init__(self):


if __name__=='__main__':
    #t =test()

    silverHonda = SUV('honda', 'CRV', 'silver', '2009', 'None')
    silverHonda.display()
    redJLR=SUV('JLR', 'discovery', 'red', '2025', 'yes')
    redJLR.display()
    newcar=car('Toyota', 'Crown', 'white', '2024')
    newcar.display()

    sedan1=Sedan("Chevy","Cobalt","Blue","2001","Auto")
    sedan2=Sedan("Mazda","Protege5","White","2002","Manual")

    sedan1.display()
    sedan2.display()