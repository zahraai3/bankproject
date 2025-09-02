
class Deposit:
  @staticmethod

  def exc(users):
    print("Alright!, you’re here to make a deposit 💰 ")
    user_name = input(" Enter your bank account name : ").lower()
    money_amount = int(input(" Enter the deposit ammount, please : "))

    found = False

    for i in users :
      if i.name == user_name :
        i.total += money_amount
        print(f"deposit successful! 💰 you deposited ${money_amount} and your new balance is ${i.total} ")
        found = True
        break
    if not found:
        print(" your user_name is not valid, try again. ")
    


  @staticmethod
  def restart(users):
     
    while True:

      done = input("Would you like to make another deposit ?(True, False): ").lower()
      if done == "true":
       Deposit.exc(users)
      elif done == "false":
       print ("Thank you for banking with us! Have a great day.")
       break
      else:
       print ("Wrong input, Enter True or False ")



