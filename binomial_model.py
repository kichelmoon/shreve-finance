import random

def flip_coins(times):
    flips = []
    for i in range(0, times):
        flip = random.randint(0, 1)
        flips.append(flip)

    return flips


class ModelParameters:
    u: float
    d: float
    r: float

    p_tilde: float
    q_tilde: float

    def check_no_arbitrage(self):
        return 0 < self.d < 1 + self.r < self.u

    def __init__(self, up_factor, interest):
        self.u = up_factor
        self.d = 1/self.u
        self.r = interest
        self.p_tilde = (1 + self.r - self.d) / (self.u - self.d)
        self.q_tilde = (1 - self.p_tilde)

class Simulation:
    parameters: ModelParameters
    number_of_steps: int
    flips: list[int]
    s_0: float
    stock_simulation: list[float]
    cash_simulation: list[float]

    def __init__(self, model_parameters, steps, initial_stock_price):
        if model_parameters.check_no_arbitrage():
            self.parameters = model_parameters
            self.number_of_steps = steps
            self.s_0 = initial_stock_price
            self.stock_simulation = []
            self.stock_simulation.append(self.s_0)
            self.cash_simulation = []
            self.cash_simulation.append(1)
            self.generate_new()
        else:
            print("Arbitrage in the model!")

    def generate_new(self):
        self.flips = flip_coins(self.number_of_steps)

        for i in range(0, self.number_of_steps - 1):
            if self.flips[i] == 0:
                self.stock_simulation.append(self.stock_simulation[-1] * self.parameters.u)
            elif self.flips[i] == 1:
                self.stock_simulation.append(self.stock_simulation[-1] * self.parameters.d)

            self.cash_simulation.append(self.cash_simulation[-1] * (1+self.parameters.r))

    def get_portfolio_simulation(self, stock_ratio):
        if 0 < stock_ratio < 1:
            portfolio = []
            for i in range(0, self.number_of_steps):
                portfolio.append(stock_ratio * self.stock_simulation[i] + (1 - stock_ratio) * self.cash_simulation[i])
            return portfolio
        else:
            return [0] * self.number_of_steps
