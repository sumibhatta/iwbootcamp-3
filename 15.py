#Imagine you are designing a banking application. What would a
#customer look like? What attributes would she have? What methods
#would she have?

class Customer:
    bank = 'Everest Bank'

    def __init__(self, name, phone, address, account_no, balance, account_type):
        self.name = name
        self.phone = phone
        self.address = address
        self.account_no = account_no
        self.balance = balance
        self.account_type = account_type
    
    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def changeAccountType(self, strr):
        self.account_type = strr

    def checkBalance(self):
        print("Balance: ", self.balance)

    def account_info(self):
        print("Bank Name: ", self.bank)
        print("Account Details: ")
        print("Name: ", self.name)
        print("Account Number: ", self.account_no)
        print("Account Type: ", self.account_type)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Balance: ", self.balance)


cus1 =Customer('Sumi','9823344556','nayabazar','000112233445566',5000000, 'savings')

cus1.account_info()
cus1.deposit(10000)
cus1.withdraw(10000)
cus1.checkBalance()
cus1.changeAccountType('Fixed')
