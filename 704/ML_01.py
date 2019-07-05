# coding:utf-8
__author__ = 'Kukafee'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    x = np.linspace(0.001, 1, 100)
    y = x ** x
    plt.plot(x, y, 'r-', linewidth=1)
    plt.show()

    # n = np.random.rand(5)
    # print(n)



    pass

if __name__ == '__main__':
    main()
