
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Số dư không hợp lệ")    

    def display(self):
        print(f"Thông tin tài khoản: {self.get_account_number()}, {self.get_account_name()}, {self.get_balance()}")

    def withdraw(self, amount):
        if 0 < amount < self._balance: 
            self._balance -= amount
        else:
            print ("Số tiền rút không hợp lệ")    

    def deposit(self, amount):
        if amount > 0: 
            self._balance += amount
        else:
            print ("Số tiền nạp không hợp lệ")    


bank_account = BankAccount("TCB", "Dinh Thi Hanh", 1000000) 
bank_account.display() 

bank_account.deposit(4000000)
bank_account.display() 

bank_account.withdraw(2000000)
bank_account.display()