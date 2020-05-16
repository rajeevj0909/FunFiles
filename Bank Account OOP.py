class BankAccount():
   def __init__(self, accountName, balance):
       self.accountName = accountName
       self.balance = balance
   
   def deposit(self):
       add=float(input("How much do you want to deposit?"))
       self.balance=self.balance+add
       return self.balance
   
   def withdraw(self):
       take=float(input("How much do you want to withdraw?"))
       self.balance=self.balance-take
       return self.balance

   def balance(self):
       return self.balance

class CheckingAccount(BankAccount):
   def __init__(self, accountName, balance,lastCheckNum):
       self.accountName=accountName
       self.balance=balance
       self.lastCheckNum=lastCheckNum
   def lastCheck(self):
        return(self.lastCheckNum)
      
class SavingsAccount(BankAccount):
   def __init__(self, accountName, balance,interestRate):
       self.accountName=accountName
       self.balance=balance
       self.interestRate=interestRate
   def savings(self):
      self.balance=self.balance*self.interestRate
      return self.balance

#class InvestmentAccount(BankAccount):
   #def __init__(self, accountName, balance):
       #self.accountName=accountName
       #self.balance=balance
   #def withdraw(self):
       #print("Donkey")

Acc_test = CheckingAccount("M Shields",0,50)
print("Your balance is now : £" ,Acc_test.deposit())
print("Your balance is now : £" ,Acc_test.withdraw())
print("Your last check is",Acc_test.lastCheck())

Acc_test = SavingsAccount("M Shields",Acc_test.balance(),1.5)
print("At the end of one year, with an intrest rate of 5% a year, you have: £",Acc_test.savings())

#Acc_test = InvestmentAccount("M Shields",0,5)
