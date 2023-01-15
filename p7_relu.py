import numpy as np


n = int(input("Enter number of neuron in hidden layer: "))
ip = np.array([],dtype=int)

size = int(input("Enter size of input array: "))
for i in range (size):
    x = int(input("Enter input: "))
    ip = np.append(ip,x)
print("Inputs are: ", ip)

def percept(n,ip):
    N = np.array([],dtype=int)
    for i in range(n):
        np.random.seed(26)
        weight = np.random.randn(n)
        print("weight are: ",weight)

        ni = (ip*weight).sum()
        na = np.maximum(0,ni)
        N = np.append(N,na)

    print("Inputs for output layer neuron: ",N)
    np.random.seed(26)
    ow = np.random.randn(n)
    print("Weights of output layer neuron are: ", ow)

    op = (N*ow).sum()
    op_act = np.maximum(0,op)
    return op_act

op = percept(n,ip)
print("Final output is: " ,op)
