from BankAccount import *

Nebiyu = BankAccount(1000, "Nebiyu")
Leul = BankAccount(2000, "Leul") 

Nebiyu.getBalance()
Leul.getBalance() 
Nebiyu.deposit(500)
Leul.withDraw(200)
Leul.withDraw(10000)
Nebiyu.Transfer(50, Leul)
Nebiyu.Transfer(20000, Leul) 

Meba = InterestRewardAcc(1000, 'Meba')
Meba.getBalance()
Meba.deposit(100)
Meba.Transfer(400, Nebiyu) 

Daniel = SavingAcc(1000, 'Daniel')
Daniel.getBalance()
Daniel.deposit(700)
Daniel.Transfer(600, Meba)
Daniel.withDraw(788)