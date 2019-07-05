# -*- coding:utf8 -*-

import math
import matplotlib.pyplot as plt

def main():
    x = [float(i)/100.0 for i in range(1, 300)]
    # x = [i for i in range(1, 3, 0.01)]
    y = [math.log(i) for i in x]
    plt.plot(x, y, 'r-', linewidth=2, label='log Curve')
    a = [x[20], x[175]]
    b = [y[20], y[175]]
    plt.plot(a, b, 'g-', linewidth=2)
    plt.plot(a, b, 'b*', markersize=10, alpha=0.75)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('log(y)')

    plt.show()

    pass

if __name__ == "__main__":
    main()