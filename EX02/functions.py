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
        x = np.insert(x, 0, values = np.ones((1,row_num)), axis = 1)
        self.theta = theta
        self.x = x
        self.y = y
        self.row_num = row_num
        self.alpha = alpha

    def set_theta(self, new_theta):
        self.theta = new_theta

    def sigmoid(self, n):
        Hx = np.zeros(shape = (100 ,1))
        i = 0
        for x in n:
            if x >= 0:
                hx = 1 / (1 + np.exp(-x))
            else:
                hx = np.exp(x) / (1 + np.exp(x))
            Hx[i] = hx
            i += 1
        return Hx
        
    def com_theta(self):
        # compute hx
        N = np.dot(self.x, self.theta)
        Hx = self.sigmoid(N)
        # compute theta
        sum_part = np.dot((Hx - self.y).T ,self.x)
        new_theta = self.theta - self.alpha / self.row_num * sum_part.T
        # compute J
        Hx = Hx + np.power(float(10),-5)
        sum_part = np.sum((self.y * np.log(Hx) + (1 - self.y) * np.log(1 - Hx)))
        j_val = -1 / self.row_num * sum_part
        return new_theta, j_val
        

        
        
    
    

    
