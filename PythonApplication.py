class CashRegister:
    def __init__(self, cash):
        self.cash = cash

    def top_up(self, x):
        self.cash += x

    def count_1000(self):
        return self.cash // 1000

    def take_away(self, x):
        if self.cash < x:
            raise ValueError(f"Unable to take away {x}: not enough cash.")
        self.cash -= x

    def get_cash(self):
        return self.cash

cash_register = CashRegister(2000)
cash_register.top_up(500)
print(cash_register.get_cash())

print(cash_register.count_1000())

cash_register.take_away(2000)
print(cash_register.get_cash())

cash_register.take_away(700)
print(cash_register.get_cash())
