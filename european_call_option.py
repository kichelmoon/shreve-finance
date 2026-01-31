import binomial_model as bm

class EuropeanCallOption:
    strike_price: float
    duration: int

    def __init__(self, strike_price, duration):
        self.strike_price = strike_price
        self.duration = duration

    def payoff(self, stock_price):
        return max(0, stock_price - self.strike_price)

    def calculate_delta(self, stock_price, parameters: bm.ModelParameters) -> float:
        stock_up_price = stock_price * parameters.u
        stock_down_price = stock_price * parameters.d
        return round((self.payoff(stock_up_price) - self.payoff(stock_down_price))/(stock_up_price - stock_down_price), 2)

    def calculate_one_turn_worth(self, stock_price, parameters: bm.ModelParameters) -> float:
        stock_up_price = stock_price * parameters.u
        stock_down_price = stock_price * parameters.d
        return 1/(1+parameters.r) * (parameters.p_tilde*self.payoff(stock_up_price) + parameters.q_tilde* self.payoff(stock_down_price))
