import numpy as np
import matplotlib.pyplot as plt
import time
 
plt.ion()
plt.figure(1)
x_list = [1,2,3]
y_list = [2,4,2]
plt.plot(x_list, y_list,c='y',ls='-', marker=',')  
plt.ioff()
plt.pause(0.5)
x_list = [2,3,4]
y_list = [2,4,5]
# plt.clf()
plt.plot(x_list, y_list,c='y',ls='-', marker=',')  
# plt.pause(0)
