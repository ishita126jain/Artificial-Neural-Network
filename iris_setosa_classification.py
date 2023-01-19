import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data[:,(2,3)]
y = (iris.target == 0).astype(np.int64) #setosa


def pred(x,w):
    return 1 if (x*w).sum() > 0 else 0

def learning(x,y,w):
    print('weight ',w)
    for k in range(10):
        print('------iteration ',k+1)
        for i,j in zip(x,y):
            if j - pred(i,w) > 0:
                w = w + 0.001* i
            elif j - pred(i,w) < 0:
                w = w - 0.001* i
            else:
                a=1
    return w

np.random.seed(11)
w = np.random.randn((len(x[0])))
w = learning(x,y,w)

#test
print('test.....')
print('test instant 1 = ',pred(x[1],w)==y[1])
print('test instant 10 = ',pred(x[10],w)==y[10])
print('test instant -1 = ',pred(x[-1],w)==y[-1])

correct,incorrect =0,0
for i,j in zip(x,y):
    if pred(np.array(i),w)==j:
        correct += 1
    else:
        incorrect += 1
accuracy =(1.0* correct)/len(x)
print('accuracy = ',accuracy*100,'%')
