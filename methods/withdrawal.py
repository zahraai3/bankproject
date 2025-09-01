class Withdrawal:
  @staticmethod
  def exc(users):
   print("Alright, you’re here for a withdrawal 💵")
   user_name = input("Enter your bank account name : ").lower()
   amount = int(input("Enter the amount you want to withdraw:"))

   for i in users:
     if i.name.lower() == user_name.lower():
       if i.total>= amount:  
         i.total -= amount
       print (f"You have withdrawn this ${amount}, and this amount remains in your account ${i.total}")


  @staticmethod
  def restart(users):
     

    while True:

      done = input("Would you like to make another withdrawal?(True, False): ").lower()
      if done == "true":
       Withdrawal.exc(users)
      elif done == "false":
       print ("Thank you for banking with us! Have a great day")
      else:
       print ("Wrong input, Enter True or False")

 
       
     
   

                 
    
   
        

