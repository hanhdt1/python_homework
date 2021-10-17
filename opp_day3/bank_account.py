class BankAccount:
    def __init__(self, account_number, owner , balance=0):
        self._account_number = account_number
        self._owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number    

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"Số tài khoản {self.account_number}\nThông tin KH: {self._owner.get_info()}\nSố dư: {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")  


class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005
   
    def calculate_interest(self):
        return self.monthly_interest_rate*self.balance

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"{self.name}, {self.date_of_birth}, {self.email}, {self.phone}"    

cus = Customer("Dinh Thi Hanh","10/06/1984","hanhdt1@gmail.com","0975752502")
bank_account = SavingAccount("100023300000", cus, 8000000) 
bank_account.display() 
print(f"Lãi: {bank_account.calculate_interest()}")