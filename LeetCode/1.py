import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Probability density of the binomial distribution
def bin_dist(k, n, p):
    nck = factorial(n) / (factorial(k) * factorial(n - k))
    pd = nck * p**k * (1-p)**(n-k)
    return pd

num1 = 100
num2 = 500
prob1 = 0.5
prob2 = 0.1

r1 = int(2*num1*prob1)
x1 = np.arange(r1)
pd1 = np.array([bin_dist(k, num1-1, prob1) for k in range(r1)])
plt.ylim(0, 0.1)
plt.bar(x1, pd1, color='lightcoral')
plt.show()

r2 = int(2*num2*prob2)
x2 = np.arange(r2)
pd2 = np.array([bin_dist(k, num2-1, prob2) for k in range(r2)])
plt.ylim(0, 0.1)
plt.bar(x2, pd2, color='lightcoral')
plt.show()