import matplotlib.pyplot as plt
import numpy as np

def plot_simulation(simulation, steps, delta_0, interest):
    x = np.arange(0, steps, 1)
    plt.plot(x, simulation[0])
    plt.plot(x, simulation[1])
    plt.plot(x, simulation[2])

    plt.legend(["Stocks", "Cash", "Portfolio with " + str(delta_0) + " parts Cash"])
    plt.title("Binomial model with " + str(interest) + " interest")
    plt.xlabel("Steps")
    plt.ylabel("Price")
    plt.show()
    plt.show()

    plt.show()
