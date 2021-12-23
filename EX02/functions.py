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


#function
class func(object):

    def __init__(self, theta, x, y, row_num = 0, alpha = 0.01):
        theta = np.array(theta)
        new_var = np.insert(new_var, 0, values = np.ones((1,row_num)), axis = 1)
        self.theta = theta
        self.x = x
        self.y = y
        self.row_num = row_num
        self.one = np.ones((1,row_num))
        self.alpha = alpha

    def set_theta(self, new_theta):
        self.theta = new_theta

    def com_theta(self):
        # compute hx
        N = np.dot(x, self.theta)
        Hx = 1 / (self.one + np.e**N)
        # compute theta
        sum_part = np.dot((Hx - self.y).T ,self.x)
        new_theta = self.theta - self.alpha / self.row_num * sum_part
        # compute J
        sum_part = np.sum((self.y * np.log(Hx) + (self.one - y) * np.log(self.one - Hx)), axis = 1)
        j_val = -1 / self.row_num * sum_part
        return new_theta, j_val
        

def vali(x, y):
    x = np.insert(x, 0, values = np.ones((1,100)), axis = 1)
    theta = np.dot((np.dot(np.linalg.inv(np.dot(x.T ,x)), x.T)),y)
    return theta 
        
        
    
    

    
