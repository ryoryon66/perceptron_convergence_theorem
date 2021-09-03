#https://starpentagon.net/analytics/simple_perceptron/
#単純パーセプトロンの収束定理

import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
#import matplotlib.animation as animation

#positive
X0 = np.array([])
Y0 = np.array([])
#negative
X1 = np.array([])
Y1 = np.array([])

cnt = 0

ans = [np.random.randint(-3,3) for i in range(3)]

for i in range(50):
    newx = np.random.randint(-7,7)
    newy = np.random.randint(-7,7)
    if ans[0]*newx + ans[1]*newy + ans[2] >= 0:
        X0=np.append(X0,[newx])
        Y0=np.append(Y0,[newy])
    else:
        X1=np.append(X1,newx)
        Y1=np.append(Y1,newy)

#print(X0)


W = np.array([0.0,0.0,0.0])


def make_gragh(nowW):

    x_line = np.array([i/10 for i in range(-61,61)])
    div = W[1]

    if nowW[1] == 0:
        div += 0.00101
        #print(45)

    y_line = np.array([ float(-nowW[2]-x*nowW[0])/float(div)  for x in x_line])
    
    
    plt.plot(x_line,y_line)
    plt.scatter(X0,Y0,s=10,label="positive",)
    plt.scatter(X1,Y1,s=10,label="negative")
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.legend()
    #global cnt
    plt.text(-10,-10,str(cnt+1),size=30)
    plt.plot(-10,-10)
    plt.show()
    plt.savefig("classification"+str(cnt+1))
    plt.cla()
    



def update(X,prevW,sign):
    RATE = 0.001
    #print( prevW + sign * X)
    global cnt
    cnt += 1
    return prevW + sign * X
    
make_gragh(W)

while True:
    is_updated = False

    for i in range(len(X0)):
        X = np.array([X0[i],Y0[i],1])
        result = (np.dot(X,W) > 0)
        if not result:
            W = update(X,W,1)
            make_gragh(W)
            is_updated = True

    for i in range(len(X1)):
        X = np.array([X1[i],Y1[i],1])
        result = (np.dot(X,W) < 0)
        if not result:
            W = update(X,W,-1)
            make_gragh(W)
            is_updated = True
    
    if not is_updated:
        break
print(ans)
print(W)


#plt.plot(X0,Y0,label="1")

print(cnt)
make_gragh(W)










