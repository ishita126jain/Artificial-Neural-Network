import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = np.array([0,1,1,1])
np.random.seed(26)
b = np.random.randint(0,10)
while 1:
    count=0
    A = np.array([])
    for i in range(4):
        a = (X[i][0]+X[i][1])-b
        A = np.append(A,a)
    for i in range(Y.size):
        if Y[i] == 1 and A[i]<0:
            b=b-1
            break
        else:
            count=count+1
            
    if count == A.size:
        break
    
print(b)
        
        
        
