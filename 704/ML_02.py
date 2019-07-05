__author__ = 'Kukafee'

import numpy as np
import matplotlib.pyplot as plt


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(0, 4, 1000)
    x, y = np.meshgrid(u, u)
    z = np.log(np.exp(x) + np.exp(y))
    ax.contourf(x, y, z, 20)
    plt.show()


    pass

if __name__ == "__main__":
    main()

