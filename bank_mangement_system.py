class Bank:
    # Initialize bank with an empty dictionary to store user account name and balance
    def __init__(self):
        self.customers={}

    def create_account(self,account_number,initial_balance=0):
        if account_number in self.customers:
            print("Account already exixts.")
        else:
            self.customers[account_number]=initial_balance
            print("Account created Successfully.")
    
    def make_deposit(self,account_number,amount):
        if account_number in self.customers:
            self.customers[account_number]+=amount
            print("Deposit Successful.")
        else:
            print("Account number does not exist.")

    def withdraw(self,account_number,amount):
        if account_number in self.customers:
            if self.customers[account_number]>=amount:
                self.customers[account_number]-=amount
                print("Withdrawal Successfull.")
            else:
                print("Not Enough fund.")
        else:
            print("Accout number does not exist.")
    
    def check_balance(self,account_number):
        if account_number in self.customers:
            balance=self.customers[account_number]
            print(f"Your balance is {balance}")
        else:
            print("Accout number does not exist.")

customer1=Bank()
customer1.create_account("1234",500)
customer1.make_deposit("1234",500)
customer1.withdraw("1234",200)
customer1.check_balance("1234")