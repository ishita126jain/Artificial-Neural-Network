import numpy as np
X = np.array([2,3])
W1 = np.array([1,1])
W2 = np.array([-1,1])
Wo = np.array([2,-1])
n1 = (X*W1).sum()
n2 = (X*W2).sum()
N = np.array([n1,n2])
no = (N*Wo).sum()

print(no)
