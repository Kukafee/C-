# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    path = '../4.Regression/iris.data'
    data = pd.read_csv(path, header=None)
    print(data.head())
    print(data.dtypes)
    print(type(data))
    print(data.columns)
    print(data.loc[0])
    print('*'*100)
    # print(data.values)
    # print(data[4])
    data[4] = pd.Categorical(data[4]).codes
    # print(data[4])
    x, y = np.split(data.values, (4, ), axis=1)
    # print(x , y)

    x = x[:,:2]
    # print(x)
    lr = Pipeline([
        ('sc', StandardScaler()),
        ('poly', PolynomialFeatures(degree=10)),
        ('clf', LogisticRegression())
    ])
    lr.fit(x, y.ravel())
    y_hat = lr.predict(x)
    y_hat_pro = lr.predict_proba(x)
    np.set_printoptions(suppress=True)
    print('y_hat = \n', y_hat)
    print('y_ravel = \n', y.ravel())
    # print('y_hat_pro = \n', y_hat_pro)
    # print(np.mean(y_hat == y.ravel()))
    acc = [y_hat == y.ravel()]
    print('acc:', np.mean(acc))
    l1 = [False, True ,False]
    print('l1:', np.mean(l1))
    print('ACC: %.2f%%'%(100*np.mean(y_hat == y.ravel())))

    N, M = 200, 200
    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)
    x_test = np.stack((x1.flat, x2.flat), axis=1)
    # ******************************************

    mpl.rcParams['font.sans-serif'] = ['simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    cm_light = mpl.colors.ListedColormap(['#77E0A0', '#FF8080', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    y_hat = lr.predict(x_test)  # 预测值
    y_hat = y_hat.reshape(x1.shape)  # 使之与输入的形状相同
    plt.figure(facecolor='w')
    plt.pcolormesh(x1, x2, y_hat, cmap=cm_light)  # 预测值的显示
    plt.scatter(x[:, 0], x[:, 1], c=y.flat, edgecolors='k', s=50, cmap=cm_dark)  # 样本的显示
    plt.xlabel(u'花萼长度', fontsize=14)
    plt.ylabel(u'花萼宽度', fontsize=14)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid()
    patchs = [mpatches.Patch(color='#77E0A0', label='Iris-setosa'),
              mpatches.Patch(color='#FF8080', label='Iris-versicolor'),
              mpatches.Patch(color='#A0A0FF', label='Iris-virginica')]
    plt.legend(handles=patchs, fancybox=True, framealpha=0.8)
    plt.title(u'鸢尾花Logistic回归分类效果 - 标准化', fontsize=17)
    plt.show()




    pass


if __name__ == '__main__':
    main()