"""
Banking system using OOP

Parent class: user
    - Holds details about an user
    - Has a function to show user details
Child class: Bank
    - Stores details about the account balance
    - Stores details about the amount
    - Allows for deposit, withdraw, view balance
    
"""

## Parent class
class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showUserDetails(self):
        print('User details:')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')


## Child class
class Bank(User):
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Account has been updated: ${self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('This operation can not be dont! You do not have enough money')
            print(f'Balance available is ${self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'You withdrawed ${self.amount}')            
            print(f'Your account is now ${self.balance}')

    def viewBalance(self):
        self.showUserDetails()
        print(f'Your account is ${self.balance}')

mamy = Bank('Mamy',23,'Male')
mamy.deposit(7000)
mamy.viewBalance()


