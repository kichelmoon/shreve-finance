import matplotlib.pyplot as plt
import random
import numpy as np

u = 2
d = 1 / u
r = 0.02

def check_discrete_no_arbitrage(u, d, r):
    return 0 < d < 1+r < u


def flip_coins(times):
    flips = []
    for i in range(0, times):
        flip = random.randint(0, 1)
        flips.append(flip)

    return flips


def calculate_binomial_stock(steps, starting_price):
    states = [starting_price]
    flips = flip_coins(steps)
    for flip in flips:
        if flip == 0:
            states.append(states[-1]*d)
        elif flip == 1:
            states.append(states[-1]*u)

    return states


def calculate_riskless(steps, starting_cash):
    states = [starting_cash]
    for i in range(0, steps):
        states.append(states[-1]*(1+r))

    return states


def calculate_wealth(steps, starting_wealth, delta, stock_states, cash_states):
    states = [starting_wealth]
    for i in range(0, steps):
        position = delta*stock_states[i] + delta*cash_states[i]
        states.append(position)

    return states


def run_simulation(number_of_steps):
    if check_discrete_no_arbitrage(u, d, r):
        y = calculate_binomial_stock(number_of_steps, S_0)
        z = calculate_riskless(number_of_steps, X_0)
        p = calculate_wealth(number_of_steps, X_0, delta_0, y, z)

        return [y, z, p]
    else:
        print("Arbitrage in the model!")
        return []


def plot_simulation(simulation, n):
    x = np.arange(0, n + 1, 1)
    plt.plot(x, simulation[0])
    plt.plot(x, simulation[1])
    plt.plot(x, simulation[2])

    plt.legend(["Stocks", "Cash", "Portfolio with " + str(delta_0) + " parts Stocks"])
    plt.title("Binomial model with " + str(r) + " interest")
    plt.xlabel("Steps")
    plt.ylabel("Price")
    plt.show()
    plt.show()

    plt.show()


n = 10
S_0 = 1
X_0 = 1
delta_0 = 0.5

simulation_results = run_simulation(n)
plot_simulation(simulation_results, n)


