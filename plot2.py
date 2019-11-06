import numpy as np
import matplotlib.pyplot as plt
wavn = np.loadtxt("C:/Users/ROUNAK/Desktop/study/recent assignments/Pending/python codes/NASA_data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (0))
Itn = np.loadtxt("C:/Users/ROUNAK/Desktop/study/recent assignments/Pending/python codes/NASA_data.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (1))
print(Itn)
print(wavn)
plt.scatter(wavn , Itn)
plt.grid()
plt.show()