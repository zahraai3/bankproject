#coloring the terminal output :)
from colorama import Fore,init,Back,Style
init()

class Withdrawal:
  @staticmethod
  def exc(users):

   print(Fore.BLUE+"Alright, you’re here to make a withdrawal 💵"+Style.RESET_ALL)

   user_name = input("Enter your bank account name : ").lower()
   amount = int(input("Enter the amount you want to withdrawal:"))

   for i in users:
     if i.name.lower() == user_name.lower():
       if i.total>= amount:  
         i.total -= amount
         print (Fore.MAGENTA+f"You have withdrawn this ${amount}, and this amount remains in your account ${i.total}"+Style.RESET_ALL)

       else:
        print (f"Sorry {i.name}, The amount you requested ${amount} is more than the money you have in your account ${i.total}")
     else:
       print("Account is not found,try again")
       Withdrawal.exc(users)

  @staticmethod
  def restart(users):
     

    while True:
      print("")
      done = input("Would you like to make another withdrawal?(True, False): ").lower()
      if done == "true":
       print("")
       Withdrawal.exc(users)
      elif done == "false":
       print("")
       print (Fore.MAGENTA+Back.WHITE+"Thank you for banking with us! Have a great day."+Style.RESET_ALL)
       break
      else:
       print ("Wrong input, Enter True or False")
      

 
       
     
   

                 
    
   
        

