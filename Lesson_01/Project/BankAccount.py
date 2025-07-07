class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\n Account '{self.name}' created. \n Balance = ${self.balance:.2f} ") 

    def getBalance(self):
        print(f"\n Account '{self.name}' Balance = $ {self.balance:.2f}")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(' Deposit complete.')
        self.getBalance() 

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:2f} "
            )
        
    def withDraw(self, amount):
       try:
           self.viableTransaction(amount) 
           self.balance = self.balance - amount
           print('\n Withdraw complete')
           self.getBalance()
       except BalanceException as error:
           print(f"\n Withdraw interrupted: {error} ")
    
    def Transfer(self, amount, account):
        try:
            print('\n ********** \n\n Beginning Transfer... 🚀 ')
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print('\n Transfer complete!✅ \n\n **********')
        except BalanceException as error:
            print(f"You can't transfer ❌ since your account only has ${self.balance:.2f}") 


class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05) 
        print('\n Deposit complete.')
        self.getBalance() 

class SavingAcc(InterestRewardAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName) 
        self.fee = 5 

    def withDraw(self, amount):
        try: 
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print('\n Withdraw completed.')
            self.getBalance() 
        except BalanceException as error: 
            print(f'Withdraw interrupted: {error}')