import numpy as np

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[1]])
w1 = np.random.randint(-10,10)
w2 = np.random.randint(-10,10)
w = np.array([w1,w2])
print("Initial value of weights: ",w)

def TLU(inp, w):
    if (inp*w).sum() > 0:
        return 1
    else:
        return 0

for epoch in range(15):
    print("epoch = ",epoch+1)
    for i, j in zip(x,y):
        if j==1 and TLU(i,w)==0:
            w[0]=w[0]-1
            w[1]=w[1]-1
        elif j==0 and TLU(i,w)==1:
            w[0]=w[0]+1
            w[1]=w[1]+1

print("Final value of weights: ",w)

