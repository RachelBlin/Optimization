import numpy as np
from scipy.optimize import newton_krylov
import matplotlib.pyplot as plt

def F(x):
    """
    Definition of the function F(x) we want to solve.
    Here we want to solve cos(x) + tan(x) + x = [1,1,1,1].
    We can convert that into solving cos(x) + tan(x) + x - [1, 1, 1, 1] = 0.
    We thus define F(x) = cos(x) + tan(x) + x - [1, 1, 1, 1].

    :param x:
    :return: The function to be solved
    """
    return np.cos(x) + np.tan(x) + x - np.array([1, 1, 1, 1])

def solver(F, xin, f_tol):
    """
    A function to solve F(x) = 0

    :param F: The function F(x) = 0 to be solved
    :param xin: The initialisation of x
    :param f_tol: The precision of the solution
    :return: The solution
    """
    x = newton_krylov(F, xin, f_tol=f_tol)
    return x

xin = [1, 1, 1, 1]
f_tol = 1e-20
x = solver(F, xin, f_tol)
# In this case, the solution of cos(x) + tan(x) + x = [1, 1, 1, 1] is [0, 0, 0, 0]
# Details:
# cos([0, 0, 0, 0]) = [1, 1, 1, 1]
# tan([0, 0, 0, 0]) = sin([0, 0, 0, 0])/cos([0, 0, 0, 0]) = [0, 0, 0, 0]
# [1, 1, 1, 1] + [0, 0, 0, 0] + [0, 0, 0, 0] = [1, 1, 1, 1]
print('Solution of cos(x) + tan(x) + x - [1, 1, 1, 1] = 0 : ', x)

# Checking the obtained solution, cos(x) + tan(x) + x - [1, 1, 1, 1] should be equal to [0, 0, 0, 0]
x_check = F(x)
print('Verifying cos(x) + tan(x) + x - [1, 1, 1, 1] = 0. F(solution) = ', x_check)


