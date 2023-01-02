import matplotlib.pyplot as plt
import numpy as np

class ChartInterface :
    def __init__(self):
        self.x_list = np.array([])
        self.y_list = np.array([])
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.plot, = self.ax.plot(self.x_list, self.y_list,c='y',ls='-', marker=',')

    def _checkUpdateList(self):
        if len(self.x_list) > 1200 :
            self.x_list = self.x_list[-1000:]
            self.y_list = self.y_list[-1000:]

    def drawing(self,x,y):
        self._checkUpdateList()
        self.x_list = np.append(self.x_list,x)
        self.y_list = np.append(self.y_list,y)
        self.plot.set_xdata(self.x_list)
        self.plot.set_ydata(self.y_list)
        self.ax.relim() 
        self.ax.autoscale_view(True,True,True)
        self.fig.canvas.draw()
        plt.pause(0.0001)
        # self.plot.set_ydata(numpy.append(self.plot.get_ydata(), new_data))

    def clear(self):
        self.x_list = []
        self.y_list = []

    def undraw(self):
        plt.clf()

    def __del__(self):
        plt.ioff()
    

plt.show()
