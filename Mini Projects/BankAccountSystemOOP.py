#INITIAL TASKS
#Allow user to
#1. Create an account
# 2. Deposit money
# 3. Withdraw amoney
# 4. Check their balance

#ENHANCEMENTS
# 1. transaction history
# 2. support multiple accounts
# 3. account lookup
# 4. Encapsulate i.e. make balance key private

#in this class the setter method of encapsulation is deposit, withdraw and the getter method is check_balance
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        # self.balance=balance
        #using balance as a public key that can be accessed from anywhere in a program is a risky method
        # it can be changed to anything 
        # so converting it to private key usind a double underscore__
        self.__balance=balance
        self.transactions=[]

    def deposit(self,amount):
        if amount>0:
          self.__balance += amount
          self.transactions.append(f"{amount} deposited")
          print(f"the new amount after deposition of {amount} : {self.__balance}")
        else:
            print("not enough amount to deposit")

    def withdraw(self,amount):
        if self.__balance>=amount:
          self.__balance -= amount
          self.transactions.append(f"{amount} withdrawn")
          print(f"the new amount after deposition of {amount} : {self.__balance}")
        else:
            print(f"not enough balance to withdraw")

    def check_balance(self):
        print(f"{self.account_holder} has {self.__balance} in their account")

    def show_transactions(self): #ENHANCED FEATURE
        print(f"transaction history for {self.account_holder}")
        if self.transactions:
            for i in self.transactions:
              print(i)
        else:
            print(f"Nothing in transaction history!!")

class BankSystem:
    def __init__(self):
        self.accounts={}

    def create_accounts(self,account_name, initial_balance):
        if account_name not in self.accounts:
           self.accounts.update({account_name: BankAccount(account_name, initial_balance)}) #BankAccount(..,..) chai object ho BankAccount class ko
           #paila esle parameter pass garcha class lai ani class le store garera return garda yo object jasari stor ehuncha
           print(self.accounts)
        else:
            print(f"Account with name {account_name} already exists!!")

    def get_accounts(self,account):
        if account in self.accounts:
            return self.accounts.get(account,None)
    

banksys1=BankSystem()

while True:
    print("\n-----Choose an option------")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show Transactions")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice=='1':
       account_name=input("enter the name of the account holder:")
       balance=float(input("Enter the initial balance:"))
       banksys1.create_accounts(account_name,balance)

    elif choice in {'2','3','4','5'}:
        name= input("Enter account holder's name:")
        bankacc1=banksys1.get_accounts(name) #account ko sabai info paucha ani as an object class BankAccount lai pass garcha
        
        bankacc1.balance=-2000 #bankacc1.accountholder will have -2000 in their account if i perform action number 4 because balance can be changed from anywhere
        #as soon as we mad ekey private this wont work

        bankacc1.__balance=-100 #using this wont be of any use too
        #this is not raising any eeror even while trying to access it using private key 
        # because __balance attribute is immediately created and python sees it as a new attr not modification of its private key attribute

        if not bankacc1:
            continue
        
        if choice=='2':
            deposit_amount=float(input("Enter the amount you wnat to deposit:"))
            bankacc1.deposit(deposit_amount)

        if choice=='3':
            withdraw_amount=input("Enter the amount you wnat to withdraw:")
            bankacc1.withdraw(withdraw_amount)

        if choice=='4':
            bankacc1.check_balance()

        if choice=='5':
            bankacc1.show_transactions()

    elif choice=='6':
        break
    else:
        print("invalid choice!!!")