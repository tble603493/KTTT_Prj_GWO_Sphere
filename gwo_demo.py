import numpy as np
import matplotlib.pyplot as plt

# Sphere function
def sphere(x):
    return np.sum(x**2)

# Grey Wolf Optimizer (GWO)
def gwo(obj_func, dim=2, n_wolves=20, max_iter=50, lb=-10, ub=10):
    # Initialize wolf positions
    X = np.random.uniform(lb, ub, (n_wolves, dim))

    # Alpha, Beta, Delta wolves
    alpha = beta = delta = None
    alpha_f = beta_f = delta_f = np.inf

    history = []

    for t in range(max_iter):

        # Evaluate wolves
        for i in range(n_wolves):
            fitness = obj_func(X[i])

            if fitness < alpha_f:
                alpha_f, alpha = fitness, X[i].copy()
            elif fitness < beta_f:
                beta_f, beta = fitness, X[i].copy()
            elif fitness < delta_f:
                delta_f, delta = fitness, X[i].copy()

        # Linearly decreasing parameter a
        a = 2 - 2 * t / max_iter

        for i in range(n_wolves):

            r1, r2 = np.random.rand(), np.random.rand()
            A1 = 2 * a * r1 - a
            C1 = 2 * r2

            r1, r2 = np.random.rand(), np.random.rand()
            A2 = 2 * a * r1 - a
            C2 = 2 * r2

            r1, r2 = np.random.rand(), np.random.rand()
            A3 = 2 * a * r1 - a
            C3 = 2 * r2

            X1 = alpha - A1 * np.abs(C1 * alpha - X[i])
            X2 = beta  - A2 * np.abs(C2 * beta  - X[i])
            X3 = delta - A3 * np.abs(C3 * delta - X[i])

            X[i] = (X1 + X2 + X3) / 3
            X[i] = np.clip(X[i], lb, ub)

        history.append(alpha_f)

    return alpha, alpha_f, history


# ----------------------------
# Run a demo on the Sphere function
# ----------------------------
if __name__ == "__main__":
    best_pos, best_val, history = gwo(sphere, dim=5, max_iter=60)

    print("Best position:", best_pos)
    print("Best value:", best_val)

    # Plot convergence
    plt.figure(figsize=(6, 4))
    plt.plot(history)
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness")
    plt.title("GWO Convergence on Sphere Function")
    plt.grid(True)
    plt.show()
