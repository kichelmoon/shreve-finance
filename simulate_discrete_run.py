import binomial_model as bm
import simulation_plots as sp

n = 10
s_0 = 1
X_0 = 1
delta_0 = 0.3

my_params = bm.ModelParameters(2, 0.02)
simulation = bm.Simulation(my_params, n, s_0)
simulation_results = [simulation.stock_simulation, simulation.cash_simulation, simulation.get_portfolio_simulation(delta_0)]
sp.plot_simulation(simulation_results, n, delta_0, simulation.parameters.r)
