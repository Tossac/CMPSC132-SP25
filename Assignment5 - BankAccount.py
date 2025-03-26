#Alex Hall
#CMPSC132 Spring 2025
#Assignment 5: BankAccount
#Implement a Python class demonstrating Encapsulation by defining private attributes and providing getter and setter methods for controlled access.



class BankAccount():
    #Initialize the account number and balance.
    def __init__(self, account_number, balance):
        self.__account_number=account_number
        self.__balance=balance

    #standard getter:
    def getAccountNumber(self):
        return self.__account_number
    
    #Ensure the account number is set only during initialization and cannot be modified externally.
    #def setAccountNumber(self, account_number):
        #self.__account_number=account_number
    #the "standard setter" for Balance should also probably be removed due to extreme risk potential
    #def setBalance(self, balance):
        #self.__balance=balance

    #Add the amount to the balance if the amount is positive.
    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            print(f"${amount:.2f} has been deposited.")
        else:
            print(f"Cannot deposit ${amount:.2f}")
            print("Please enter a positive amount to deposit.")
        print()

    #Deduct the amount from the balance if sufficient funds are available.
    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"${amount:.2f} has been withdrawn.")
        else:
            print(f"Insufficient funds to withdraw ${amount:.2f}")
        print()
    
    #Return the current balance.
    def get_Balance(self):
        return self.__balance
    
    #is the only private method that calculates the accrued interest based on the interest rate and the balance.
    #The formula to use for the interest is  = (balance * interest_rate)/1200
    def __calculate_interest(self, interest_rate):
        return (self.__balance * interest_rate)/1200
    
    #A public function that will call the __calculate_interest function with the interest_rate to calculate the interest on the current balance and
        #print the interest calculated by the __caculate_interest function.
    def getInterest(self, interest_rate):
        print(f"Current interest accrued is ${self.__calculate_interest(interest_rate):.2f}")
    


def main():
    #testing suite:
    print("TESTING: Bank Account.py")
    newAccount = BankAccount(12345, 1000)

    #(iii) Print the balance using get_balance - (a) at the beginning,
    print(f"Current balance is: ${newAccount.get_Balance():.2f}")

    #(i) performing deposit,
    #invalid
    newAccount.deposit(-1000)
    newAccount.deposit(0)
    #valid
    newAccount.deposit(1000)

    #(iii) Print the balance using get_balance - (b) after calling the deposit,
    print(f"Current balance is: ${newAccount.get_Balance():.2f}")

    #(ii) withdraw transactions,
    #invalid
    newAccount.withdraw(5000)
    #valid
    newAccount.withdraw(1000)

    #(iii) Print the balance using get_balance - (c) after calling withdraw.
    print(f"Current balance is: ${newAccount.get_Balance():.2f}")

    #(iv) Finally, call get interest with a 10% interest to calculate the accrued interest on the balance and print the interest out.
    newAccount.getInterest(10)

    #Ensure the account number is set only during initialization and cannot be modified externally.
    newAccount.__account_number=98765
    print(f"Account number: {newAccount.getAccountNumber()}")


if __name__=="__main__":
    main()

"""Implement a Python class demonstrating encapsulation by defining private attributes and providing getter and setter methods for controlled access.

1. Create a class `BankAccount` with the following attributes:
    __account_number (private member)
    __balance  (private member)

    

2. Next, Implement the following methods:
__init__(self, account_number, balance):
    Initialize the account number and balance.

deposit(self, amount):
    Add the amount to the balance if the amount is positive.

withdraw(self, amount):
    Deduct the amount from the balance if sufficient funds are available.

get_balance(self):
    Return the current balance.

__calculate_interest(self, interest_rate):
    is the only private method that calculates the accrued interest based on the interest rate and the balance.
    The formula to use for the interest is  = (balance * interest_rate)/1200
    
getInterest(self, interest_rate):
    A public function that will call the __calculate_interest function with the interest_rate to calculate the interest on the current balance and
        print the interest calculated by the __caculate_interest function.

        

3. Ensure the account number is set only during initialization and cannot be modified externally.
    Also, the __calculate_interest is a private method, so it cannot be directly called from the main. 


    
4. Demonstrate the class usage by creating an object of account class
    (i) performing deposit,
    (ii) withdraw transactions,
    (iii) Print the balance using get_balance - (a) at the beginning, (b) after calling the deposit, and (c) after calling withdraw.
    (iv) Finally, call get interest with a 10% interest to calculate the accrued interest on the balance and print the interest out.  

 

Rubric :
    (a) Implementing private variables: 5 (pt)
    (b) Implementing all five public methods (except for the private method) correctly: (50 pt)
    (c) Implementing the private method __calculate_interest correctly : (15pt)
    (d) Creating an object and testing:             
        (i) performing deposit (5 pt)
        (ii) withdraw transactions (5 pt)
        (iii) Print the balance using get_balance - (a) at the beginning, (b) after calling the deposit, and (c) after calling withdraw. (10 pt)
        (iv) Finally, call get interest with a 10% interest to calculate the accrued interest on the balance and print the interest out. (10 pt)
"""