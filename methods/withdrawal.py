class Withdrawal:
  @staticmethod
  def exc(users):

   user_name = input("Enter your bank account name : ").lower()
   amount = int(input("Enter the amount you want to withdraw:"))

   for i in users:
     if i.name.lower() == user_name.lower():
       i.total -= amount
       print (f"You have withdrawn this ${amount}, and this amount remains in your account ${i.total}")
     
   

                 
    
   
        

