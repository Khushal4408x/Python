from abc import ABC , abstractmethod
class Account(ABC):
    def __init__(self,account_number,account_holder_id,initial_balance=0.0):
        self.account_number=account_number
        self.account_holder_id=account_holder_id
        self.balance=initial_balance
    @abstractmethod
    def deposit(self,amount): pass
    @abstractmethod
    def withdraw(self,amount): pass
    def display_details(self):
        return f"Account number: {self.account_number} Balance: Rs. {self.balance}"
class Savings_Account(Account):
    interest_percent=5
    Time=None
    def deposit(self, amount):
            if(amount<0):
                 return "Enter valid amount"
            self.balance+=amount
            return "Deposit successful"
    def withdraw(self, amount):
        if(amount<0):
             return "Enter valid amount"
        if(self.balance-amount>=0):
             self.balance-=amount
             return "Withdraw Successful"
        else:
             return("Insufficient Balance !") 
    def set_time(self,time):
         self.Time=time             
    def apply_interest(self):
         if(self.Time==None):
              return ("Time not defined !")
         elif(self.balance>0):
             interest=(self.balance*self.interest_percent*self.Time)/100
             self.balance+=interest
class Current_Account(Account):
      overdraft=0
      overdraftLimit=150000
      def deposit(self, amount):
            if(amount<0):
                 return "Enter valid amount"
            self.balance+=amount
            return "Deposit successful"
      def withdraw(self, amount):
        if(amount<0):
             return "Enter valid amount"
        if(self.balance-amount>=0):
             self.balance-=amount
             return "Withdraw Successful"
        
             
        
        
             
             
                     