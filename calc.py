import numpy as np
from utils import *


def get_newton_raphson_root(eq, df):
    max_iter = 20  # Max iterations
    tol = 0.0001  # Tolerance
    i = 0  # Iteration counter
    x0 = 3  # Initial guess
    xi_1 = x0
    print("Iteration" + str(i) + ": x = " + str(x0) + ", f(x) = " +
          str(get_eq_abs_value(eq, "x", x0, false)))

    while i < max_iter:
        while get_eq_abs_value(eq, "x", xi_1, false):
            xi = xi_1 - get_eq_abs_value(eq, "x", xi_1, false) / get_eq_abs_value(df, "x", xi_1, false)  # Newton-Raphson equation
            print("Iteration " + str(i) + ": x = " + str(xi) + ", f(x) = " +
                  str(get_eq_abs_value(eq, "x", xi, false)))
            xi_1 = xi
            x1_1 = np.round(xi_1, 4)
            break
        i = i + 1
