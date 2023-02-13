#Create a bank account class with methods for deposit, withdrawal, and checking the balance. 
class bank_account:
    def __init__(self,name,deposit_amount,withdrawal_amount):
        self.name = name
        self.deposit_amount = deposit_amount
        self.withdrawal_amount = withdrawal_amount
    def deposit(self):
        return f"{self.name} deposited the {self.deposit_amount}"
    def withdrawal(self):
        return f"{self.name} withdrawal the {self.withdrawal_amount}"
    def check_balance(self):
        return f"the remaining balance is {self.name} account is {self.deposit_amount-self.withdrawal_amount}"
shubham = bank_account("shubham",10000,9000)
print(shubham.deposit())
print(shubham.withdrawal())
print(shubham.check_balance())