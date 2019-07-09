# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

s = 0.001
def main():
    x = np.linspace(s, 1-s, 100)
    # print(x)
    y = -x * np.log(x) - (1-x) * np.log(1-x)

    plt.plot(x, y, 'r-', lw=2)
    plt.show()

    pass


if __name__ == "__main__":
    main()