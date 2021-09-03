#https://starpentagon.net/analytics/simple_perceptron/
#単純パーセプトロンの収束定理

import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
#import matplotlib.animation as animation





#線形分離の基準となる直線 ans[0]x + ans[1]y + ans[2] = 0
ans_line = [np.random.randint(-3,3) for i in range(3)]

#data
#positive
X0 = np.array([])
Y0 = np.array([])
#negative
X1 = np.array([])
Y1 = np.array([])

#パラメータの初期化　バイアスW[2]
W = np.array([0.0,0.0,0.0])

# 学習回数
cnt = 0


#線形分類可能なデータを生成する。
def generate_data(line):
    #positive
    global X0, Y0, X1, Y1
    X0 = np.array([])
    Y0 = np.array([])
    #negative
    X1 = np.array([])
    Y1 = np.array([])

    #データの生成
    for i in range(50):
        newx = np.random.randint(-7,7)
        newy = np.random.randint(-7,7)
        if line[0]*newx + line[1]*newy + line[2] >= 0:
            X0=np.append(X0,[newx])
            Y0=np.append(Y0,[newy])
        else:
            X1=np.append(X1,newx)
            Y1=np.append(Y1,newy)
    
    return

def make_gragh(nowW,isFinal = False):

    #直線を描く処理
    x_line = np.array([i/10 for i in range(-101,101)])
    div = nowW[1]

    if nowW[1] == 0:
        div += 0.00101
        #print("zero dividing")

    y_line = np.array([ float(-nowW[2]-x*nowW[0])/float(div)  for x in x_line])
    plt.plot(x_line,y_line)

    #散布図
    plt.scatter(X0,Y0,s=10,label="positive",c = "orange")
    plt.scatter(X1,Y1,s=10,label="negative", c = "blue")
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.legend()
 
    plt.text(-10,-10,str(cnt),size=30)
    plt.plot(-10,-10)
    #plt.show()
    plt.savefig("classification"+str(cnt))
    if isFinal:
        plt.savefig("final_result")

    plt.cla()
    
def update(incorrect_point,prevW,category):
    global cnt
    cnt += 1
    RATE = 0.001
    if category == 1:
        return prevW + RATE * incorrect_point
    else:
        return prevW - RATE * incorrect_point

generate_data(ans_line)
    
make_gragh(W)

while True:
    is_updated = False

    for i in range(len(X0)):
        X = np.array([X0[i],Y0[i],1])
        result = (np.dot(X,W) >= 0)
        if not result:
            W = update(X,W,1)
            make_gragh(W)
            is_updated = True

    for i in range(len(X1)):
        X = np.array([X1[i],Y1[i],1])
        result = (np.dot(X,W) < 0)
        if not result:
            W = update(X,W,0)
            make_gragh(W)
            is_updated = True
    
    if not is_updated:
        break


print(ans_line)
print(W)
print(cnt)
make_gragh(W,isFinal = True)

import make_gif










