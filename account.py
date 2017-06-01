class Account:
	def __init__(self, acc_no, balance=0.0):
		self.acc_no = acc_no
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		
	def display(self):
		return "Account No. :" + str(self.acc_no) + "\n" + "Balance = " + str(self.balance)	
	


class Savings(Account):
	def __init__(self, acc_no):
		Account.__init__(self, acc_no)
		
	def display(self):
		return "Account Type: Savings" + "\n" + Account.display(self)		

	def Withdraw(self, amount):
		if amount > self.balance or self.balance < 15000: print ("Insufficient Balance")
		else: self.balance = self.balance - amount
		return self.balance
	
			
			
class Current(Account):
	def __init__(self, acc_no):
		Account.__init__(self, acc_no)

	def display(self):
		return "Account Type: Current" + "\n" + Account.display(self)
			
	def Withdraw(self, amount):
		if amount > self.balance or self.balance < 15000: print ("Insufficient Balance")
		else: self.balance = self.balance - amount - (amount*0.1)
		return self.balance
