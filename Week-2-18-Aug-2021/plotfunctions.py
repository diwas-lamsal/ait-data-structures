# Diwas Lamsal - st122324
# 2021-August-18 Data Structures and Algorithms Week 2
# Question: Graph the functions 1, n, n^2, sqrt(n), n log n, n^3, 2^n using python

# import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------- Initialize Variables -------------------------------------- #

# I learned that float128 does not currently work with windows
# But using float64 causes an overflow in our y=2n function and throws a runtime warning
x = np.logspace(0, 15, 100, dtype=np.float64)
y_1 = np.ones(100)
y_n = x
y_square = x * x
y_squareroot = np.sqrt(x)
y_nlogn = x * np.log(x)
y_cube = x ** 3
y_2n = 2 ** x

# -------------------------------------- Plot The Data -------------------------------------- #

fig = plt.figure()
p = fig.add_subplot(1, 1, 1)
p.set_yscale('log')
p.set_xscale('log')
p.set_xlim(1, 10 ** 15)
p.set_ylim(1, 10 ** 19)

# Plot all the functions in the graph
p.plot(x, y_1, label='1')
p.plot(x, y_n, label='n')
p.plot(x, y_square, label='square')
p.plot(x, y_squareroot, label='squareroot')
p.plot(x, y_nlogn, label='nlogn')
p.plot(x, y_cube, label='cube')
p.plot(x, y_2n, label='2n')

# Show the legend and the plot
plt.legend()
plt.show()
