class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        
    def deposit(self, amount):
        assert amount > 0, '必須是大於 0 的正數'
        self.balance += amount
        
    def withdraw(self, amount):
        assert amount > 0, '必須是大於 0 的正數'
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')
    def displayMoney(self):
        print("there are",self.balance,"money now.")
a = Account('E122', 'Justin')
a.displayMoney()
a.deposit(1)
a.displayMoney()
a.deposit(-1)    # AssertionError: 必須是大於 0 的正數
a.displayMoney()