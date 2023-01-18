import numpy as np

x = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0],[1],[1],[1],[1],[1]])
b = np.random.randint(-10,10)
print("Initial value of b: ",b)
def TLU(inp, b):
    if sum(inp) > b:
        return 1
    else:
        return 0

for epoch in range(15):
    print("epoch = ",epoch+1)
    for i, j in zip(x,y):
        if j==1 and TLU(i,b)==0:
            b=b-1
        elif j==0 and TLU(i,b)==1:
            b=b+1

print("Final value of b: ",b)

