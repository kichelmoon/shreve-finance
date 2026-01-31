class EuropeanCallOption:
    strike_price: float
    def __init__(self, strike_price):
        self.strike_price = strike_price

    def payoff(self, stock_price):
        return max(0, stock_price - self.strike_price)

