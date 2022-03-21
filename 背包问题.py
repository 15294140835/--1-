#0/1背包问题
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time
'''++++++++++++++++++++++++①++++++++++++++++++++++++++'''

#第一步数据导入与检查
f = open("Y:\软件工程\测试数据\\beibao0-9.in",'r+')  #打开文件
print("请输入你要处理的数据为第几组：")
group = int(input())
lnum = 0
for line in f:             #按行读取
    lnum += 1

        #获取物品数量n
        s = line.strip().split(' ')
        n = str(s[3])
        n = n.strip().split('d=3*')
        n = str(n[1])
        n = n.strip().split(',')
        n = 3* int(n[0])
        print("物品数量 n = ：",n)
        #获取背包容量c
        c = str(s[-1])
        c = c.strip().split('.')
        c = int(c[0])
        print("背包容量 c = ：",c)
    #获取各个物品价值存入V中

        V = line.strip().split(',')
        Vv = V[-1].split('.')
        V[-1] = Vv[0]
        #print("物品价值 V = ：",V)
    #获取各个物品重量存入W中

        W =  line.strip().split(',')
        Ww = W[-1].split('.')
        W[-1] = Ww[0]
        #print("物品重量 W = ",W)


'''++++++++++++++++++++++++②+++++++++++++++++++++++++'''
#绘制任意一组D{0-1}KP数据以重量为横轴、价值为纵轴的数据散点图；
x = []    #物品重量
w = []
y = []    #物品价值
v = []
for i in range(n):
    x = int(W[i])
    w.append(x)
    y = int(V[i])
    v.append(y)
    plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("W")
plt.ylabel("V")
plt.show()


'''++++++++++++++++++++++++③+++++++++++++++++++++++++'''
#对一组D{0-1}KP数据按项集第三项的价值:重量比进行非递增排序；
V_W = []   #价值:重量比
for i in range(n):
    b = int(V[i]) / int(W[i])
    V_W.append(b)
#print(V_W)
WoPin = []
for i in range(n):
    WoPin.append(i+1)
#print(WoPin)
W_P_V_W = dict(zip(V_W,WoPin))
#print(W_P_V_W)
V_W.sort(reverse = True)
#print(V_W)
print("对一组D{0-1}KP数据按项集第三项的价值:重量比进行非递增排序如下：")
for i in V_W:
    print(W_P_V_W[i],end =' ')

data = open("结果.txt","w")  #创建保存结果文件


'''++++++++++++++++++++++++④+++++++++++++++++++++++++'''
#用户能够自主选择动态规划算法、回溯算法求解指定D{0-1} KP数据的最优解和求解时间（以秒为单位）
start = time.time()
value = [[0 for j in range(c + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, c + 1):
        if j < w[i - 1]:
            value[i][j] = value[i - 1][j]
        else:
            value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])
print('\n最大价值为:', value[n][c])

data.write('最大价值为:  ')       #写入文件
data.write(str(value[n][c]))

x = [0 for i in range(n)]
j = c
for i in range(n, 0, -1):
    if value[i][j] > value[i - 1][j]:
        x[i - 1] = 1
        j -= w[i - 1]
print('背包中所装物品为:')
data.write('\n背包中所装物品为:')   #写入文件
for i in range(n):
    if x[i]:
        print('第', i+1, '个,', end='')
        s = str(i+1) + " "     #写入文件
        data.write(s)
end = time.time()
print("\n循环运行时间:%.2f秒"%(end-start))

'''++++++++++++++++++++++++⑤+++++++++++++++++++++++++'''
#任意一组D{0-1} KP数据的最优解、求解时间和解向量可保存为txt文件或导出EXCEL文件。
data.write("\n循环运行时间:")
data.write(str(end - start))
data.write("秒")
data.close()
