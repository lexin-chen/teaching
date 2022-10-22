x1 = np.linspace(0,1,300)
y1=2*np.sin(10*math.pi*x1)**2
f2 = interp1d(x1, y1, kind = 'cubic')
#x_n=np.linspace(0,10,30)
y2=1
#print(y1)
#b = make_interp_spline(x1,y1)
plt.plot(x1, y1, c ='blue',label='n=10')
plt.xlabel("Position (x/L)")
plt.ylabel('Probability Distribution ' r'$(\psi^2/L)$')
plt.axhline(y=1, color='r', linestyle='--',label='classical')
plt.legend()
plt.show()
