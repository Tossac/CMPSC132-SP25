#Alex Hall
#CMPSC 132 SP25
#Assignment 4 - Account.py

"""
Write a Python program to implement  ‘Account’,  ‘SavingsAccount’, and ‘CheckingAccount’.
Account is the base class, and SavingsAccount and CheckingAccount are the derived classes from Account.

Each class should have a printInfo function to print the data for each class.
In your program, create at least one object of each account type to test your program.
By testing, you must call the printInfo function on all three objects and the other functions you have implemented.
"""

class Account():
    #The member VARIABLES in Account are: accountNum, currentBalance, numberOfTransactions
    def __init__(self, accountNum, currentBalance, numberOfTransactions=0):
        self.accountNum = accountNum
        self.currentBalance = float(currentBalance)
        self.numberOfTransactions = int(numberOfTransactions)

    def printInfo(self):
        print("Account number:", self.accountNum)
        print("Current Balance:", f"${self.currentBalance:,.2f}")
        print("Number of transactions:", self.numberOfTransactions)

    #The member FUNCTIONS in Account are: deposit(), withdraw()"""
    def deposit(self, depositAmount):
        #test for negative amounts
        while (depositAmount<0):
            #adding a default value so that program does not halt on repeated tests.
            print("Negative Amount detected. Default value of $1.00 entered")
            depositAmount=1
            #depositAmount=float(input("Please enter a non-negative amount to deposit. "))
        
        #confirm successful deposit
        print("Successfully deposited",f"${depositAmount:,.2f}")
        self.currentBalance+=depositAmount
        self.numberOfTransactions+=1
        print("Current Balance:", f"${self.currentBalance:,.2f}")

    def withdraw(self, withdrawAmount):
        #test for negative amounts
        while (withdrawAmount<0):
            #adding a default value so that program does not halt on repeated tests.
            print("Negative Amount detected. Default value of $1.00 entered")
            withdrawAmount=1
            #withdrawAmount=float(input("Please enter a non-negative amount to withdraw. "))

        #Check for sufficient funds
        if withdrawAmount > self.currentBalance:
            print("Insufficient Funds to withdraw", f"${withdrawAmount:,.2f}")
            
        else:
            #confirm successful withdrawal
            print("Successfully withdrew",f"${withdrawAmount:,.2f}")
            self.currentBalance-=withdrawAmount
            self.numberOfTransactions+=1
            
        print("Current Balance:", f"${self.currentBalance:,.2f}")

"""Class SavingsAccount has two new member VARIABLES
savingsBalance 
annualInterestRate

and two new member FUNCTIONS
culate_MonInterest() 
    The culate_MonInterest() should compute the following:
    monthlyInterest = (savingsBalance * annualInterestRate) / 1200;
get_Balance()
    The get_Balance() function should return the savingsBalance 
"""

class SavingsAccount(Account):
    #initialize common variables with call to super(), intialize special variables individually
    def __init__(self, accountNum, currentBalance, numberOfTransactions, savingsBalance, annualInterestRate):
        super().__init__(accountNum, currentBalance, numberOfTransactions)
        self.savingsBalance = float(savingsBalance)
        self.annualInterestRate = float(annualInterestRate)
        
    def printInfo(self):
        #use base class printInfo() for common attributes, print special variables individually
        super().printInfo()
        print("Savings Account Balance:", f"${self.savingsBalance:,.2f}")
        print("Annual Interest Rate:", self.annualInterestRate,"%")

    #since annualInterestRate is given as a whole number, must divide by 100 to convert to perecent, then divide by 12 to find monthly interest
    def calculate_MonInterest(self):
        monthlyInterest = (self.savingsBalance * self.annualInterestRate) / 1200
        print("Your Savings Interest for this month is:", f"${monthlyInterest:,.2f}")
        

    def get_Balance(self):
        return self.savingsBalance
    
    def deposit(self, depositAmount):
        #use allfunctionality from super class deposit(), but check if the savingsBalance should be increased based off of new maximum amount.
        super().deposit(depositAmount)
        if self.currentBalance>self.savingsBalance:
            self.savingsBalance=self.currentBalance
    
"""Class CheckingAccount has two VARIABLES and no additional member functions: MinBalance, Overdraftfees."""

class CheckingAccount(Account):
    #initialize common variables with call to super(), intialize special variables individually
    def __init__(self, accountNum, currentBalance, numberOfTransactions, MinBalance=1000, Overdraftfees=25):
        super().__init__(accountNum, currentBalance, numberOfTransactions)
        #forcing int() here as I've never seen Minimum Balances or Overdraft Fees that were not whole numbers
        self.MinBalance = int(MinBalance)
        self.Overdraftfees = int(Overdraftfees)

    def printInfo(self):
        #use base class printInfo() for common attributes, print special variables individually
        super().printInfo()
        print("Minimum Balance:", f"${self.MinBalance:,.2f}")
        print("Overdraft Fees:", f"${self.Overdraftfees:,.2f}")

    #alert customer if current balance is below minimum
    #overload deposit() and withdraw(), but still use all of the standard functionality
    def deposit(self, depositAmount):
        super().deposit(depositAmount)
        belowMin(self.currentBalance, self.MinBalance)

    def withdraw(self, withdrawAmount):
        super().withdraw(withdrawAmount)
        belowMin(self.currentBalance, self.MinBalance)

def test(testAccount):
    #will test different Variables/Functions based on account type:
    #standard Account tests on all objects that have base type Account.
    if type(testAccount) is Account or type(testAccount) is SavingsAccount or type(testAccount) is CheckingAccount:
        print("Testing Account#:", testAccount.accountNum)
        print()
        print("Testing printInfo():")
        testAccount.printInfo()
        print()

        #Test Account Variables
        print("Testing Account Variables:")
        print(testAccount.accountNum)
        print(f"${testAccount.currentBalance:,.2f}")
        print(testAccount.numberOfTransactions)
        print()

        #Test Account Functions
        print("Testing Account Functions:")
        testAccount.deposit(testAccount.currentBalance/2)
        #negative deposit
        testAccount.deposit(-1)

        #allowable withdrawl
        testAccount.withdraw(testAccount.currentBalance/3)

        #disallowed withdrawl
        #too big
        testAccount.withdraw(testAccount.currentBalance*4)
        #negative
        testAccount.withdraw(-1)
        print()

        #SavingsAccount specific tests
        if type(testAccount) is SavingsAccount:
            #Test SavingsAccount Variables
            print("Testing Savings Account Variables:")
            print(f"${testAccount.savingsBalance:,.2f}")
            print(testAccount.annualInterestRate,"%")
            print()

            #Test SavingsAccount Functions
            print("Testing Savings Account Functions:")
            print(f"${testAccount.get_Balance():,.2f}")
            testAccount.calculate_MonInterest()
            #test for successful update of savingsBalance
            testAccount.deposit(testAccount.currentBalance*2)
            print(f"${testAccount.get_Balance():,.2f}")
            testAccount.calculate_MonInterest()
            print()

        #CheckingAccount specific tests
        if type(testAccount) is CheckingAccount:
            #Test CheckingAccount Variables
            print("Testing Checking Account Variables")
            print(f"${testAccount.MinBalance:,.2f}")
            print(f"${testAccount.Overdraftfees:,.2f}")

            #Test CheckingAccount Functions
            print("Testing Checking Account Functions")
            #test for Account being brought below minimum
            testAccount.withdraw(testAccount.currentBalance-testAccount.MinBalance+1)
            print()


        #print post-test values
        print("Post-test of Account#: ", testAccount.accountNum)
        testAccount.printInfo()


    else:
        print("Object is not an Account")

    print()

def getUserAccount():
    accountType = ""
    while(accountType!="B" and accountType!="S" and accountType!="C"):
        accountType=input("Would you like to create a (B)asic, a (S)avings, or a (C)hecking Account?").upper()

    accountNumber=input("What is the account number? ") #TODOadd a test for previously established account numbers, would need to pass list of accounts to this function
    currentBalance=input("What is the current balance? ")
    while currentBalance<0:
        currentBalance=input("Cannot establish account with negative balance. Please enter non-negative balance: ")

    if accountType=="B":
        userAccount = Account(accountNumber, currentBalance, 0)

    elif accountType=="S":
        savingsBalance=input("What is the Savings balance? ")
        if currentBalance>savingsBalance:
            savingsBalance=currentBalance

        interestRate=input("What is the annual Interest rate? ")
        userAccount = SavingsAccount(accountNumber, currentBalance, 0, savingsBalance, interestRate)

    else:
        minimumBalance=input("What is the minimum balance? ")
        if minimumBalance<0:
            minimumBalance=0
        overdraft=input("What is the overdraft fee? ")
        if overdraft<0:
            overdraft=0
        userAccount = CheckingAccount(accountNumber, currentBalance, 0, minimumBalance, overdraft)
        #test for minimum balance requirement. 
        belowMin(currentBalance, minimumBalance)

    return userAccount

def belowMin(current, minimum):
    if current<minimum:
        print("Your current balance of", f"${current:,.2f}", "is less than the required minimum balance of", f"${minimum:,.2f}",".")
        print("Please deposit enough money to bring your account to the minimum in the next 30 days.")
    

def main():
    #Establish new Accounts of various types
    newAccount = Account("12345", 13000.00, 0)
    newSavingsAccount = SavingsAccount("67890", 130000.00, 0, 130000.00, 4.33)

    #accept default Minimum Balance and OD Fees of 1000 and 25, respectively
    newCheckingAccount = CheckingAccount("09876", 1300, 0)
    #high-risk/low credit rating customer: increase minimums and fees to double default value
    newHighRiskChecking = CheckingAccount("54321", 3000, 0, 2000, 50)
    
    

    #test all new accounts and 2 non-Account types
    print("This is only a test")
    test(newAccount)
    test(newSavingsAccount)
    test(newCheckingAccount)
    test(newHighRiskChecking)
    test(3)
    test("Not an Account")

    #user-defined Account
    if (input("Would you like to (C)reate a new account or (E)xit?").upper()=="C"):
        userDefinedAccount = getUserAccount()
        test(userDefinedAccount)


if __name__ == "__main__":
    main()

"""
Write a Python program to implement  ‘Account’,  ‘SavingsAccount’, and ‘CheckingAccount’.
Account is the base class, and SavingsAccount and CheckingAccount are the derived classes from Account.

Each class should have a printInfo function to print the data for each class.
In your program, create at least one object of each account type to test your program.
By testing, you must call the printInfo function on all three objects and the other functions you have implemented.

The member VARIABLES in Account are:
accountNum
currentBalance
numberOfTransactions

The member FUNCTIONS in Account are
deposit()
withdraw()


Class SavingsAccount has two new member VARIABLES
savingsBalance 
annualInterestRate

and two new member FUNCTIONS
culate_MonInterest() 
    The culate_MonInterest() should compute the following:
    monthlyInterest = (savingsBalance * annualInterestRate) / 1200;
get_Balance()
    The get_Balance() function should return the savingsBalance 


Class CheckingAccount has two VARIABLES and no additional member functions
MinBalance 
Overdraftfees.


Make sure to write __init__ method in all three classes where
the CheckingAccount or SavingsAccount class __init__ function should call the Account class __init__ method to initialize the common variables.

Also, the printInfo function of the CheckingAccount or SavingsAccount class should
call the printInfo of the Account class to print the common attribute. 


printInfo for Account class should print the attributes
accountNum
currentBalance
numberOfTransactions


printInfo for SavingsAccount class should print the attributes
accountNum
currentBalance
numberOfTransactions
savingsBalance 
annualInterestRate


printInfo for CheckingAccount class should print the attributes
accountNum
currentBalance
numberOfTransactions
MinBalance 
Overdraftfees.
"""