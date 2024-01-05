import numpy as np
import matplotlib.pyplot as plt
# Source: https://github.com/tirthajyoti/Stats-Maths-with-Python/blob/master/Brownian-motion-with-Python.ipynb

# Inputs to brownian motion
steps = 50  # total steps in random walk
x0 = 0  # initial state
W = [0] * steps  # state at each step
# ----------------------------------------------------------------------------------------------------------------------
# Generate random walk
# ----------------------------------------------------------------------------------------------------------------------
def random_walk(x0, total_steps=100):
    # Warning about the small number of steps
    if total_steps < 30:
        print("The number of steps is small. It may not generate a good stochastic process sequence")
    W = np.ones(total_steps) * x0
    for i in range(1, total_steps):
        # Sampling from the Normal distribution with probability 1/2
        yi = np.random.choice([1, -1])
        # Weiner process
        W[i] = W[i - 1] + (yi / np.sqrt(total_steps))
    return W
# ----------------------------------------------------------------------------------------------------------------------
# Generate samples from normal distribution
# ----------------------------------------------------------------------------------------------------------------------
def normal_distribtuion(x0, total_steps=100):
        if total_steps < 30:
            print("The number of steps is small. It may not generate a good stochastic process sequence")
        W = np.ones(total_steps) * x0
        for i in range(1, total_steps):
            # Sampling from the Normal distribution
            yi = np.random.normal()
            # Weiner process
            W[i] = W[i - 1] + (yi / np.sqrt(total_steps))
        return W

# ----------------------------------------------------------------------------------------------------------------------
# Generate a Stock Prices using Wiener Process
# ----------------------------------------------------------------------------------------------------------------------
def stock_price(x0, s0=100, mu=0.2, sigma=0.68, deltaT=52,dt=0.1):
        """
        Models a stock price S(t) using the Weiner process W(t) as
        `S(t) = S(0).exp{(mu-(sigma^2/2).t)+sigma.W(t)}`

        Arguments:
            s0: Iniital stock price, default 100
            mu: 'Drift' of the stock (upwards or downwards), default 1
            sigma: 'Volatility' of the stock, default 1
            deltaT: The time period for which the future prices are computed, default 52 (as in 52 weeks)
            dt (optional): The granularity of the time-period, default 0.1

        Returns:
            s: A NumPy array with the simulated stock prices over the time-period deltaT
        """
        n_step = int(deltaT / dt)
        time_vector = np.linspace(0, deltaT, num=n_step)
        # Stock variation
        stock_var = (mu - (sigma ** 2 / 2)) * time_vector
        # Set the initial value to zero for the stock price simulation
        x0 = 0
        # Weiner process (calls the `normal_distribtuion` method)
        weiner_process = sigma * normal_distribtuion(n_step)
        # Add two time series, take exponent, and multiply by the initial stock price
        s = s0 * (np.exp(stock_var + weiner_process))

        return s
# ----------------------------------------------------------------------------------------------------------------------
# Utility Function
# ----------------------------------------------------------------------------------------------------------------------
def plot_stock_price(mu,sigma):
    plt.figure(figsize=(9,4))
    for i in range(5):
        plt.plot(b.stock_price(mu=mu,
                               sigma=sigma,
                               dt=0.1))
    plt.legend(['Scenario-'+str(i) for i in range(1,6)],
               loc='upper left')
    plt.hlines(y=100,xmin=0,xmax=520,
               linestyle='--',color='k')
    plt.show()