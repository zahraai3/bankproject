class Transfer:
    @staticmethod #نضيفه حته نكوللهم ان هالكلاس مانستخدمه حته ننشا منه كاىنات وانما لاستخدام منفصل 
    def exc(users):
       print("Alright, you’re here for a transfer 🔄")
       user_name = input("Enter your bank account name : ")

       user_account = None
       for i in users:
           if i.name.lower() == user_name.lower():
               user_account = i
               break
           
       if user_account == None:
           print("Account is not found,try again")
       else:
           second_user_name = input("Enter the bank account name you want to transfer the money for : ")

           second_user_account = None

           for i in users:
             if i.name.lower() == second_user_name.lower() and i.name.lower() != user_name.lower():
               second_user_account = i
               break
       if second_user_account == None:
           print("Account is not found,try again")
       else :
           money_amount = int(input("Enter the amount u want to transfer : "))
           money = money_amount

           if money > user_account.total :
               print("There are not enough funds for the transfer.")
           else :
               user_account.total -= money
               second_user_account.total += money
               print(f"A total of ${money} had been transfered from {user_name.upper()} to {second_user_name.upper()},your new balance is: ${user_account.total}")
               
    @staticmethod
    def restart(users):
     
     while True:

      done = input("Would you like to make another Transfer?(True, False): ").lower()
      if done == "true":
       Transfer.exc(users)
      elif done == "false":
       print ("Thank you for banking with us! Have a great day")
       break
      else:
       print ("Wrong input, Enter True or False")

 
           

