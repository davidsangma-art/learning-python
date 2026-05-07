# Write code below 💖
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name=first_name
    self.last_name=last_name
    self.account_id=account_id
    self.pin=pin
    self.balance=balance

  
  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    self.balance -=amount
    return amount

  def display_balance(self):
    print(f"current balance: ${self.balance:.2f}")

my_account=BankAccount("Joe","Doe",123456,"Saving",2324,200)
my_account.deposit(96)
my_account.withdraw(25)
my_account.display_balance()
