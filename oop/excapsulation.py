class bankAccount:
  def __init__(self, balance):
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount

  def get_balance(self):
    return self.balance

account = bankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500