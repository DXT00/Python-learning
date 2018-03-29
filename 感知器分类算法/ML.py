# -*- coding: utf-8 -*-
import numpy as np #数据处理
import pandas as pd
import matplotlib.pyplot as plt #数据可视化的库
from matplotlib.colors import ListedColormap
class Perception(object):
    """
    eta:学习率
    n_iter:权重向量训练次数
    w_:神经分叉权重向量
    errors_:用于记录神经元判断出错次数
    """
    def __init__(self,eta = 0.01,n_iter=10):
        self.eta=eta
        self.n_iter = n_iter

    def fit(self, X,y):
        """
         输入训练数据，进行神经元培训
         X：输入的电信号向量-->x1,x2,x3...
         y:对应样本的分类

         X:shape[n_samples,n_features]
         n_samples:有多少输入样本
         n_features：每个样本有多少个电信号（神经元的分叉数）
         X:[[1,2,3],[4,5,6]]
         n_samples:2
         n_features：3

         y:[1,-1]
         代表X中的[1,2,3]的分类是1
                [4,5,6]的分类是-1
        初始化权重向量为0
        加1是因为前面算法提到的w0,也就是步调函数的阈值
        """
        self.w_ = np.zeros(1+X.shape[1])
        self.errors_= []


        for _ in range(self.n_iter):
         #Python中对于无需关注其实际含义的变量可以用_代替，
         # 这就和for  i in range(5)一样，因为这里我们对i并不关心，所以用_代替仅获取值而已
            errors = 0
            # X:[[1,2,3],[4,5,6]]
            # y:[1,-1]
            #
            # zip(X,y)= [([1, 2, 3], 1), ([4, 5, 6], -1)]
            for xi,target in zip(X,y):
                # update = g * (y-y')
                update = self.eta * (target-self.predict(xi))
                # xi是一个向量
                # update * xi 等价：
                # deltaW[1] = X[1]*update,deltaW[2] = X[2]*update,deltaW[3] = X[3]*update
                self.w_[1:]+=update *xi
                #w1,w2,w3......

                self.w_[0] += update
                # w_[0]是阈值
                errors += int(update !=0.0)
                self.errors_.append(errors)

    def net_input(self,X):
        # z = W0*1 + W1*X1 + ......Wn*Xn
        return np.dot(X,self.w_[1:])+self.w_[0]

    def predict(self,X):
        return  np.where(self.net_input(X) >= 0.0, 1, -1)



def plot_decision_regions(X,y,classifier,resolution=0.02):
    marker = ('s','x','o','v')
    colors = ('red','blue','lightgreen','gray','cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #y只有两种取值--> -1或1 所以len(np.unique(y))=2

    x1_min,x1_max = X[:,0].min()-1,X[:,0].max()
    x2_min,x2_max = X[:,1].min()-1,X[:,1].max()
    #取出X的第0列和第1列的最小值-1，最大值
    # print(x1_min,x1_max)
    # print(x2_min,x2_max)

    #得到两个扩充后的二维矩阵
    xx1,xx2= np.meshgrid(np.arange(x1_min,x1_max,resolution),np.arange(x2_min,x2_max,resolution))

    # print(np.arange(x2_min,x2_max,resolution).shape)
    # print(np.arange(x2_min,x2_max,resolution))
    # print(xx2.shape)
    # print(xx2)
    Z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    print(xx1.ravel())
    print(xx2.ravel())
    print(Z)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z,alpha=0.4,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.xlim(xx2.min(),xx2.max())

    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0],y=X[y==cl,1],alpha=0.8,c=cmap(idx),
                    marker=marker[idx],label =cl)




def main():

    # file = r'C:/Users/DXT-/Desktop/机器学习/iris.data'
    # df = pd.read_csv(file,header=None)
    # df.head(10)
    file = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

    df= pd.read_csv(file,header=None)

    y = df.loc[0:100,4].values #把0~100行数据的第四列抽取出来
    y = np.where(y == 'Iris-setosa',-1,1)#把字符串转化为数字

    X = df.loc[0:100,[0,2]].values
    print(X)#把0~100行数据的第0列和第2列的数据抽出来
    # print(y)
    #
    # #把0~50条数据的第0列和第1列拿出来画图，用红色的o表示
    # plt.scatter(X[:50,0],X[:50,1],color='red',marker='o',label='setosa')
    # #把50~100条数据的第0列和第1列拿出来画图，用蓝色的x表示
    # plt.scatter(X[50:100,0],X[50:100,1],color='blue',marker='x',label='versicolor')
    # plt.xlabel('花瓣长度')
    # plt.ylabel('花茎长度')
    # plt.legend(loc='upper left')
    # plt.show()

    ppn=Perception(eta=0.1,n_iter=10)
    ppn.fit(X,y)
    # plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
    # plt.xlabel('Epochs')
    # plt.ylabel('错误分类次数')
    # # plt.show()


    plot_decision_regions(X,y,ppn,resolution=0.02)
    plt.xlabel('花瓣长度')
    plt.ylabel('花茎长度')
    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    main()