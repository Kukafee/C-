# -*- coding:utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0.05, 3, 0.05)
    y1 = [math.log(a, 1.5) for a in x]
    y2 = [math.log(a, 2) for a in x]
    y3 = [math.log(a, 3) for a in x]
    plt.plot(x, y1, linewidth=2, color='#007500', label='log1.5(x)')
    plt.plot(x, y2, linewidth=2, color='#9F35FF', label='log2(x)')
    plt.plot(x, y3, linewidth=2, color='#F75000', label='log3(x)')
    plt.plot([1, 1],[y1[0], y1[-2]], 'r--', linewidth=2)
    plt.grid(True)
    plt.legend(loc='lower right')
    plt.show()

    pass


if __name__ == "__main__":
    main()