from xlrd import open_workbook
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter

# 3D绘图函数
def zzt(data):
    # 设置坐标
    X = np.arange(0, 16, step=1)  # X轴的坐标
    Y = np.arange(0, 4, step=1)  # Y轴的坐标
    Z = np.array(data)

    xx, yy = np.meshgrid(X, Y)  # 网格化坐标
    X, Y = xx.ravel(), yy.ravel()  # 矩阵扁平化
    bottom = np.zeros_like(X)  # 设置柱状图的底端位值
    Z = Z.ravel()  # 扁平化矩阵

    # 每一个柱子的长和宽
    width = height = 1

    # 三维绘图设置
    fig = plt.figure()
    ax = fig.gca(projection='3d')  # 三维坐标轴
    ax.bar3d(X, Y, bottom, width, height, Z, shade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z(mean)')
    plt.setp(ax.get_xminorticklabels(), visible=False)
    plt.show()


FileName = '剔除去噪插值2020.xlsx'
wb = open_workbook(FileName)
sheets = wb.sheet_names()

m = len(sheets)
n = pd.read_excel(FileName, sheet_name=sheets[0]).shape[1] - 1
arr = np.empty((m, n))
# 循环遍历所有sheet
for i in range(len(sheets)):
    df = pd.read_excel(FileName, sheet_name=sheets[i])
    d = df.mean()

    data = []
    for j in range(1, len(d)):
        data.append(d.iat[j])

    le = n
    while(len(data) < le):
        data.append(0)

    arr[i] = data

if __name__ == "__main__":
    zzt(arr)
