# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def main():
    u = np.random.uniform(0.0, 1.0, 100000)
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()

    times = 100000
    for time in range(times):
        u += np.random.uniform(0.0, 1.0, 100000)
    print(len(u))
    u /= times
    print(len(u))
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()
    pass



if __name__ == "__main__":
    main()