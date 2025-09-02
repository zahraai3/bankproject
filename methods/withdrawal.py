from colorama import Fore,Style,init,Back
init()

class Withdrawal:
  @staticmethod
  def exc(users):
   print(Fore.CYAN+"Alright, you’re here for a withdrawal 💵"+Style.RESET_ALL)
   user_name = input("Enter your bank account name : ").lower()
   amount = int(input("Enter the amount you want to withdrawal:"))

   for i in users:
     if i.name.lower() == user_name.lower():
       if i.total>= amount:  
         i.total -= amount
         print (f"You have withdrawn this ${amount}, and this amount remains in your account ${i.total}")

       else:
        print (f"Sorry {i.name}, The amount you requested ${amount} is more than the money you have in your account ${i.total}")
       

  @staticmethod
  def restart(users):
     

    while True:

      done = input("Would you like to make another withdrawal?(True, False): ").lower()
      if done == "true":
       Withdrawal.exc(users)
      elif done == "false":
       print (Fore.MAGENTA+Back.WHITE +"Thank you for banking with us! Have a great day"+Style.RESET_ALL)
       break
      else:
       print ("Wrong input, Enter True or False")
      

 
       
     
   

                 
    
   
        

