class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i["amount"]
    return balance

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.category}")
      category.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def __str__(self):
    title = f"{self.category.center(30, '*')}\n"
    items = ""
    for i in self.ledger:
      items += f"{i['description'][:23].ljust(23)} {format(i['amount'],'.2f').rjust(7)}\n"
    total = f"Total: {format(self.get_balance(), '.2f')}"
    return title + items + total

def create_spend_chart(categories):
  print(categories)