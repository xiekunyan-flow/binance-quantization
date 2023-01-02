import matplotlib.pyplot as plt
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
from data.chart import ChartInterface as chart
import time

t = 0
lastTime = time.time()
begTime  = lastTime 
chart_test_input = chart()
while True:
    if t >= 300 * np.pi:
        # plt.clf()
        t = 0
    else:
        ntime = time.time()
        print("t is" ,t,"to last time",ntime-lastTime,"total time",ntime-begTime)
        lastTime = ntime
        t += np.pi / 4
        chart_test_input.drawing(t,np.sin(t))
        #plt.plot(t, np.sin(t), 'o')
