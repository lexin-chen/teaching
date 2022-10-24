import matplotlib.pyplot as plt
import numpy as np
import math

# Defining my interval 
x1 = np.linspace(0,1,300) #(start,stop,offset); the large amount of steps will give that smoothened line
# Defining the function to solve for that interval
y1 = 2 * np.sin(10 * math.pi * x1)**2 
# Defining function #2
y2 = 1
#Plotting the graph
plt.plot(x1, y1, c ='blue',label='n=10')
plt.xlabel("Position (x/L)")
plt.ylabel('Probability Distribution ' r'$(\psi^2/L)$')
plt.axhline(y=1, color='r', linestyle='--',label='classical')
plt.legend()
plt.show()
