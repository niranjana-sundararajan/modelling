import matplotlib.pyplot as plt
import numpy as np

# plt.close('all')
np.random.seed(0)  # Set seed


def generate_uncorrelated_random_samples(no_samples=10000, distribution="normal", plot=True, return_vals=True):
    # Sample from normal distibution
    if distribution == "normal":
        # Pick random samples of shape no_samples * 1
        S1 = np.random.normal(0, 1, no_samples)
        S2 = np.random.normal(0, 1, no_samples)

        E_S1 = np.mean(S1)
        Var_S1 = np.mean(S1 ** 2) - E_S1 ** 2
        sigma_S1 = np.sqrt(Var_S1)
        E_S2 = np.mean(S2)
        Var_S2 = np.mean(S2 ** 2) - E_S2 ** 2
        sigma_S2 = np.sqrt(Var_S2)
        Cov_S1_S2 = np.mean(S1 * S2) - E_S1 * E_S2
        Corr_S1_S2 = Cov_S1_S2 / sigma_S1 / sigma_S2
        print('corr(S1,S2) = ' + str(Corr_S1_S2))

    # Sample from Uniform Distribtuion
    if distribution == "uniform":
        # Pick random samples of shape no_samples * 1
        U1 = np.random.rand(no_samples, 1)
        U2 = np.random.rand(no_samples, 1)

        # Random samples (normally distributed uncorrelated)
        S1 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
        S2 = np.sqrt(-2 * np.log(U1)) * np.sin(2 * np.pi * U2)

        E_S1 = np.mean(S1)
        Var_S1 = np.mean(S1 ** 2) - E_S1 ** 2
        sigma_S1 = np.sqrt(Var_S1)
        E_S2 = np.mean(S2)
        Var_S2 = np.mean(S2 ** 2) - E_S2 ** 2
        sigma_S2 = np.sqrt(Var_S2)
        Cov_S1_S2 = np.mean(S1 * S2) - E_S1 * E_S2
        Corr_S1_S2 = Cov_S1_S2 / sigma_S1 / sigma_S2
        print('corr(S1,S2) = ' + str(Corr_S1_S2))

    if plot:
        # Generate plots
        plt.subplot(1, 2, 1)
        plt.plot(S1, S2, linestyle="", marker="o", color="blue")
        plt.xlabel('S1', fontsize=16)
        plt.ylabel('S2', fontsize=16)
        plt.show()

    if return_vals:
        return S1, S2


S1, S2 = generate_uncorrelated_random_samples(plot=False)


def generate_samples_with_corr_roh(S1, S2, no_samples=100000, rho=0.8, plot=True):
    mu_s1 = np.mean(S1)
    mu_s2 = np.mean(S2)

    sigma_s1 = np.sqrt(np.mean(S1 ** 2) - mu_s1 ** 2)
    sigma_s2 = np.sqrt(np.mean(S2 ** 2) - mu_s2 ** 2)

    X = mu_s1 + sigma_s1 * S1
    Y = mu_s2 + sigma_s2 * (rho * S1 + np.sqrt(1 - rho ** 2) * S2)

    mu_x = np.mean(X)
    mu_y = np.mean(Y)
    sigma_x = np.sqrt(np.mean(X ** 2) - mu_x ** 2)
    sigma_y = np.sqrt(np.mean(Y ** 2) - mu_y ** 2)

    Cov_X_Y = np.mean(X * Y) - mu_x * mu_y
    Corr_X_Y = Cov_X_Y / (sigma_x * sigma_y)

    print('corr(X,Y) = ' + str(Corr_X_Y))
    if plot:
        plt.subplot(1, 2, 2)
        plt.plot(X, Y, linestyle="", marker="o", color="green")
        plt.xlabel('X', fontsize=16)
        plt.ylabel('Y', fontsize=16)
        plt.show()


generate_samples_with_corr_roh(S1, S2)
