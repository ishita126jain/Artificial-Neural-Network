import numpy as np

n = int(input("Enter number of neuron in hidden layer: "))
ip = np.array([],dtype=int)
W = np.array([],dtype=int)
N = np.array([],dtype=int)

size = int(input("Enter size of input array: "))
for i in range (size):
    x = int(input("Enter input: "))
    ip = np.append(ip,x)
print("Inputs are: ", ip)

for i in range(n):
    weight = np.array([],dtype=int)
    for i in range(size):
        x = int(input("Enter weight: "))
        weight= np.append(weight,x)
    print("weight are: ",weight)

    W = np.append(W,weight,axis=0)
    ni = (ip*weight).sum()
    N = np.append(N,ni)

W = np.array(W).reshape(n,size)
print("weights of hidden layers are: ",W)
    

def percept(n,ip,W,N):
    
    ow = np.array([],dtype=int)
    for i in range (n):
        x = int(input("Enter weight: "))
        ow = np.append(ow,x)
    print("Weights of output layer neuron are: ", ow)

    op = (N*ow).sum()
    return op

op = percept(n,ip,W,N)
print("Final output is: " ,op)
