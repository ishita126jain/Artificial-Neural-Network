import numpy as np

x = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,1,0],[1,0,1],[1,1,1]])
y = np.array([[0],[0],[0],[0],[0],[0],[1]])
w = np.array([0.1,0.1,0.1])#np.random.randn((len(x[0])))
def pred(x,w):
    return 1 if (x*w).sum() > 0 else 0

def learning(x,y,w):
    print('weight ',w)
    for k in range(100):
        print('------iteration ',k+1)
        for i,j in zip(x,y):
            if j[0] - pred(i,w) > 0:
                w = w + 1.0* i
            elif j[0] - pred(i,w) < 0:
                w = w - 1.0* i
    return w

w = learning(x,y,w)

#test
print('test.....')
for i in x:
    print(pred(i,w))
