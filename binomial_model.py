import matplotlib.pyplot as plt
import random
import numpy as np

u = 2
d = 1 / u
r = 0.02

def flip_coins(times):
    flips = []
    for i in range(0, times):
        flip = random.randint(0, 1)
        flips.append(flip)

    return flips


def run_simulation(number_of_steps):
    if 0 < d < 1+r < u:
        flips = flip_coins(number_of_steps)

        states: list[list[float]] = [[S_0], [X_0], [X_0]]
        for i in range(0, number_of_steps):
            if flips[i] == 0:
                states[0].append(states[0][-1] * d)
            elif flips[i] == 1:
                states[0].append(states[0][-1] * u)

            states[1].append(states[1][-1] * (1+r))

            states[2].append(delta_0 * states[0][-1] + (1 - delta_0) * states[1][-1])

        return states
    else:
        print("Arbitrage in the model!")
        return []


def plot_simulation(simulation, steps):
    x = np.arange(0, steps + 1, 1)
    plt.plot(x, simulation[0])
    plt.plot(x, simulation[1])
    plt.plot(x, simulation[2])

    plt.legend(["Stocks", "Cash", "Portfolio with " + str(delta_0) + " parts Cash"])
    plt.title("Binomial model with " + str(r) + " interest")
    plt.xlabel("Steps")
    plt.ylabel("Price")
    plt.show()
    plt.show()

    plt.show()


n = 10
S_0 = 1
X_0 = 1
delta_0 = 0.3

simulation_results = run_simulation(n)
plot_simulation(simulation_results, n)
