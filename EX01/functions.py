# Some functions used in homework

from matplotlib import pyplot as plt
import numpy as np

# Scatter plot to validate the correction 
# size is the plot size of dots, marker is the shape of dots 
def scatter_plot(x1,x2, y, size = 10, marker = '*', color = 'red', x_label = ' ', y_label = ' ',theta=[]):
    plt.scatter(x1,y,s = size, marker = marker, c = color)
    plt.scatter(x2,y,s = size, marker = marker, c = color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if theta:
        plt.plot(x1, theta[0] + theta[1] * x1 + theta[2] * x2)
        plt.plot(x2, theta[0] + theta[1] * x1 + theta[2] * x2)
    plt.show()

# linear plot
def plot(x, y, x_label, y_label):
    plt.plot(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


# Derivative function
class func(object):

    def __init__(self, theta, var, row_num = 0):
        theta = np.array(theta)
        for index,row in var.iterrows():
            if index == 0:
                new_var = np.array(row)
            else:
                new_var = np.row_stack((new_var,row))
        new_var = np.insert(new_var, 0, values = np.ones((1,row_num)), axis = 1)
        self.theta = theta
        self.var = new_var
        self.row_num = row_num

    def set_theta(self, new_theta):
        self.theta = new_theta
        
    def sum_part(self,theta_flag = 0):
        sum = 0
        for i in range(self.row_num):
            sum = sum + (np.sum(self.var[i][0:-1] * self.theta.T) - self.var[i][-1]) * self.var[i][theta_flag]
        return sum / self.row_num

    def j(self):
        sum = 0
        for i in range(self.row_num):
            sum = sum + np.power((np.sum(self.var[i][0:-1] * self.theta.T) - self.var[i][-1]),2)
        return sum / (2 * self.row_num)



        
    
    

    
