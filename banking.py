class Banking:
    def __init__(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.balance=0
    def display(self):
        print()
        print("*****Account Details*****")
        print("Account Holder Name: ",self.name)
        print("Account Number: ",self.acc_no)
    def Deposit(self,amt):
        self.balance=self.balance+amt
        print("Amount Depositted! ")
    def Withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("Amount Withdrawed, Balance Updated.")
        else:
            print("Insufficient Balance")
    def View_balance(self):
        print(self.balance)
    
name=input("Enter your name: ")
acc_no=int(input("Enter the account number: "))
obj=Banking(name,acc_no)
obj.display()
print()
print()
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")
print()

while(True):
    n=int(input("Enter Your Choice: "))
    if n==1:
        amt=int(input("Enter the amount to deposit: "))
        obj.Deposit(amt)
    if n==2:
        w=int(input("Enter the amount to be withdrawed: "))
        obj.Withdraw(w)
    if n==3:
        obj.View_balance()
    if n==4:
        print("Exit!")
        break
else:
    print("Invalid Choice!")
    

        
