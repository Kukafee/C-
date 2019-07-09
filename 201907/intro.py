# !/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import CubicSpline
import math

def residual(t, x, y):
    return y - (t[0] * x**2 + t[1] * x + t[2])

def residual2(t, x, y):
    print(t[0], t[1])
    return y - t[0]*np.sin(t[1]*x)

# x**x   x > 0
# (-x) ** (-x)  x < 0
def f(x):
    y = np.ones_like(x)
    i = x > 0
    y[i] = np.power(x[i], x[i])
    i = x < 0
    y[i] = np.power(-x[i], -x[x])
    return y

def main():
    #
    # a = np.arange(0, 60, 10).reshape((-1,1)) + np.arange(6)
    # print("a = \n", a)
    # L = [1, 2, 3, 4, 5 ,6]
    # print('L = ', L)
    # a = np.array(L)
    # print("a = ", a)
    # print(type(a))
    # b = np.array([[1, 2, 3, 4],
    #               [5, 6, 7, 8,],
    #               [9, 10, 11, 12]])
    # print("b = \n", b)
    # print(type(b))
    # print(a.shape)
    # print(b.shape)
    # b.shape = (4,3)
    # print(b)
    # print(b.shape)
    # # b.shape = (2, 6)
    # # print(b)
    # b.shape = (2, -1)
    # print(b)
    # print(b.shape)
    # b.shape = (3, 4)
    # print(b.shape)
    # print(type(b))
    # print(b)
    # c = b.reshape((4, -1))
    # print("b = \n", b)
    # print("c = \n", c)
    # b[0][1] = 20
    # print("b = \n", b)
    # print("c = \n", c)
    # print(a.dtype)
    # print(b.dtype)
    # d = np.array([[1, 2, 3, 4],
    #               [5, 6, 7, 8],
    #               [9, 10, 11, 12]], dtype=np.float)
    # f = np.array([[1, 2, 3, 4],
    #               [5, 6, 7, 8],
    #               [9, 10, 11, 12]], dtype=np.complex)
    # print("d = \n", d)
    # print('f = \n', f)
    # f = d.astype(np.int)
    # print('f = \n', f)

    # print(type(d))
    # print(d.dtype)
    # d.dtype = np.int
    # print(d.dtype)
    # print(d)
    # a = np.array([1, 2, 3, 4])
    # print(a)

    # a = np.arange(1, 10, 0.5)
    # print(a)
    # print(a.dtype)
    # b = np.linspace(1, 10, 10, endpoint=False)
    # print('b = \n', b)
    # print(b.dtype)
    # d = np.logspace(1, 10, 10, endpoint=True, base=5)
    # print('d = \n', d)
    # # for i in range(10):
    # #     print(i)
    # #     for j in range(5):
    # #         print(j, end=' ')
    # f = np.logspace(0, 10, 11, endpoint=True, base=2)
    # print('f = \n', f)
    # s = 'abcd'
    # t = list(s)
    # print(t)
    # g = np.fromstring(s, dtype=np.int8)
    # print('g = \n', g)

    # a = np.arange(10)
    # print(a)
    # print(a[2])
    # print(a[3:6])
    # print(a[3:])
    # print(a[:5])
    # print(a[3:])
    # print(a[1:9:2])
    # print(a[::-1])
    # print(a)
    # a[1:4] = 10, 20, 30
    # print(a)
    # b = a[2:5]
    # b[0] = 200
    # print('b = \n', b)
    # print('a = \n', a)
    #

    # a = np.logspace(0, 9, 10, base=2)
    # print('a = \n', a)
    # i = np.arange(0, 10, 2)
    # print('i = \n', i)
    # b = a[i]
    # print(b)
    # b[2] = 1.6
    # print('b = ', b, '\na = ', a)

    # a = np.random.rand(10)
    # print('a = ', a)
    # print(a > 0.5)
    # b = a[a > 0.5]
    # a[a > 0.5] = 0.5
    # print('b = \n', b)
    # print('a = \n', a)
    #

    # a = np.arange(0, 60, 10)
    # print('a = \n', a)
    # b = a.reshape((-1, 1))
    # print('b = \n', b)
    # c = np.arange(6)
    # print('c = \n', c)
    # f = b + c
    # print('f = b + c\n', f)

    # a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
    # print ('f = \n', a)
    # # print(a[(0, 1, 2, 3), (2, 3, 4, 5)])
    # print(a[3:, [0, 2, 5]])
    # i = np.array([True, False, True, False, False, True])
    # print('a = \n', a)
    # print('a[i] = \n', a[i])
    # print(a[i, 3])

    # 139:30








    pass


if __name__ == "__main__":
    main()