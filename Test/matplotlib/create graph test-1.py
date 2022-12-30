#importing the required libraries
from math import exp
import matplotlib.pyplot as plt 

#defining the tanh function using equation 1
def tanh(x):
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

#input to the tanh function
input = []
for x in range(-5, 5):
    input.append(x)

#output of the tanh function
output = []
for ip in input:
    output.append(tanh(ip))

#plotting the graph for tanh function
plt.plot([1,1,10,10,1], [1,10,10,1,1])
# plt.grid()
#adding labels to the axes
plt.title("tanh activation function")
plt.xlabel('hhhhhhghhhhhh')
plt.ylabel('tanh(x)')
plt.show()