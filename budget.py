class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.total = 0

   

    def __str__(self):
        
      displayer = ""
      fline = self.name
      fline = fline.center(30, "*").rstrip()
      displayer = displayer + fline + '\n'
      for items in self.ledger:
          item = list(items.values())
          spart = item[0]
          spart = str('%.2f' % spart)
          fpart = item[1]
          fpart = fpart[: 23].ljust(23)
          spart = spart[: 7].rjust(7)
          displayer = displayer + fpart + spart + "\n"
      displayer = displayer + "Total: " + str('%.2f' % self.total)
      return displayer

    def deposit(self, amount, description=""):
        self.total += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        self.total -= amount
        self.ledger.append({"amount": -amount, "description": description})

        return self.check_funds(amount)

    def get_balance(self):
        return self.total

    def transfer(self, amount, instance):
        self.total -= amount
        self.ledger.append({"amount": -amount, "description": "Transfer to " + instance.name})

        instance.total += amount
        instance.ledger.append({"amount": amount, "description": "Transfer from " + self.name})

        return self.check_funds(amount)

    def check_funds(self, amount):
        return amount <= self.total


def create_spend_chart(categories):
    return None

    def deposit(self, amount, description=""):
      self.total += amount
      self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=""):
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})

      return self.check_funds(amount)
        
    def get_balance(self):
      return self.total

    def transfer(self, amount, instance):
      
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": "Transfer to " + instance.name})

      instance.total += amount
      instance.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
      
      return self.check_funds(amount)
      
    def check_funds(self, amount):
      
      return amount <= self.total

    def get_withdrawals(self):
      total = 0
      for items in self.ledger:
        if items["amount"] > 0:
          total += items["amount"]
        return total
        


def create_spend_chart(categories):

  output = "Percentage spent by category\n"

 
  total      = 0
  expenses   = []
  labels     = []
  len_labels = 0

  for item in categories:
    expense    = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
    total     += expense

    if len(item.name) > len_labels:
      len_labels = len(item.name)

    expenses.append(expense)
    labels.append(item.name)

 
  expenses = [(x/total)*100 for x in expenses]
  labels   = [label.ljust(len_labels, " ") for label in labels]

 
  for c in range(100,-1,-10):
    output += str(c).rjust(3, " ") + '|'
    for x in expenses:
      output += " o " if x >= c else "   "
    output += " \n"

  
  output += "    " + "---"*len(labels) + "-\n"

  for i in range(len_labels):
    output += "    "
    for label in labels:
      output += " " + label[i] + " "
    output += " \n"

  return output.strip("\n")
        
      