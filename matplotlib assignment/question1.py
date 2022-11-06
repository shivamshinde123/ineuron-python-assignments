import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def sine_func(x,a,b,c):
    return a*np.sin((x-b)*(np.pi/6))+c


months = list(range(0,12))
max_temp = [39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25]
min_temp = [ 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18]

constants1 = curve_fit(sine_func,months,max_temp)

a1 = constants1[0][0]
b1 = constants1[0][1]
c1 = constants1[0][2]

constants2 = curve_fit(sine_func,months,min_temp)

a2 = constants2[0][0]
b2 = constants2[0][1]
c2 = constants2[0][2]


fit1 = []
fit2 = []

for i in months:
    fit1.append(sine_func(i,a1,b1,c1))
    fit2.append(sine_func(i,a2,b2,c2))

plt.scatter(months,max_temp,label="original max temperatures")
plt.plot(months,fit1, label="fitted max temperatures")

plt.scatter(months,min_temp,label="original min temperatures")
plt.plot(months,fit2,label="fitted min temperatures")

plt.xlabel("Months")
plt.ylabel("Temperature")

plt.grid()
plt.legend()
plt.show()

