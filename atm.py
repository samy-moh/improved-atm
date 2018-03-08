class ATM():
	def __init__(self,balance,bank_name):
		self.balance = balance
		self.bank_name = bank_name

	def withdraw(self,amount):
		if amount <= 0:
			print "Error , Please Enter Vailed Amount"
		else:
			if amount <= self.balance:
				print 'Welcome To : ' + self.bank_name
				print 'Current Balance : ' + str(self.balance)
				print '================================='
				print 'Your Current Balance is : ' + str(self.balance - amount)
				while amount > 0:
					if amount >= 100:
						print 'give 100'
						amount -= 100
					elif amount >= 50:
						print 'give 50'
						amount -= 50
					elif amount >= 20:
						print 'give 20'
						amount -= 20
					elif amount >= 10:
						print 'give 10'
						amount -= 10
					elif amount >= 5:
						print 'give 5'
						amount -= 5
					elif amount < 5:
						print 'give 1'
						amount -= 1

			else:
				print 'Welcome to : ' + self.bank_name
				print '================================='
				print "NO SUFFICIENT FUNDS"