import matplotlib.pyplot as plt

import numpy as np
 
import math

x1 = np.linspace(0,1,300)
y1=2*np.sin(10*math.pi*x1)**2
f2 = interp1d(x1, y1, kind = 'cubic')
y2=1

plt.plot(x1, y1, c ='blue',label='n=10')
plt.xlabel("Position (x/L)")
plt.ylabel('Probability Distribution ' r'$(\psi^2/L)$')
plt.axhline(y=1, color='r', linestyle='--',label='classical')
plt.legend()
plt.show()
