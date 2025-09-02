from methods.withdrawal import Withdrawal
from methods.deposit import Deposit
from methods.transfer import Transfer

#class to create users with the same properties
class BankAcc:
    def __init__(self,name:str,id:int,total:int,):
        self.name = name
        self.id = id
        self.total = total

#main class to control all the actions :)
class AllBankWork:
    user1 = BankAcc('zoy',1,82000)
    user2 = BankAcc('rafal',2,73000)
    user3 = BankAcc('tabarak',3,92000)

    users =[user1,user2,user3]

    def operates(method):
        if method == 'deposit':
            Deposit.exc(AllBankWork.users)
            Deposit.restart(AllBankWork.users)
        elif method == 'withdrawal':
            Withdrawal.exc(AllBankWork.users)
            Withdrawal.restart(AllBankWork.users)
        elif method == 'transfer' :
            Transfer.exc(AllBankWork.users)
            Transfer.restart(AllBankWork.users)



print("****** NeoFuture Bank ****** 🏛️")


print("Welcome to our bank! What service do you need today?")
themwthode = input("Choose an action (withdrawal,deposit,transfer):  ").lower()
actions = ['withdrawal','deposit','transfer']

# a loop for the situation where the users want to be funny and write wrong actions :|
while themwthode not in actions:
    themwthode = input("Invalid action, please Choose an action from (withdraw,deposit,transfer):  ").lower()
AllBankWork.operates(themwthode)