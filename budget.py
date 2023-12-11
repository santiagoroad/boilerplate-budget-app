class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def getbalance(self):
    balance = 0
    for i in self.ledger:
      balance += i["amount"]
    return balance

  def check_funds(self, amount):
    if amount > self.getbalance():
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

# def create_spend_chart(categories):