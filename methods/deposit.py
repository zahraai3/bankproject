#coloring the terminal output :)
from colorama import Fore,init,Back,Style
init()


class Deposit:
  @staticmethod

  def exc(users):
    print(Fore.BLUE+"Alright!, you’re here to make a deposit 💰 "+Style.RESET_ALL)
    user_name = input(" Enter your bank account name : ").lower()
    money_amount = int(input(" Enter the deposit ammount, please : "))

    found = False

    for i in users :
      if i.name == user_name :
        i.total += money_amount
        print(Fore.MAGENTA+f"deposit successful! 💰 you deposited ${money_amount} and your new balance is ${i.total} "+Style.RESET_ALL)
        found = True
        break
    if not found:
        print(" your user_name is not valid, try again. ")
    


  @staticmethod
  def restart(users):
     
    while True:
      print("")
      done = input("Would you like to make another deposit ?(True, False): ").lower()
      if done == "true":
       print("")
       Deposit.exc(users)
      elif done == "false":
       print("")
       print (Fore.MAGENTA+Back.WHITE+"Thank you for banking with us! Have a great day."+Style.RESET_ALL)
       break
      else:
       print ("Wrong input, Enter True or False ")



