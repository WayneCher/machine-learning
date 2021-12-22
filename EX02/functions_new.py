theta = np.array(theta)
x = df['Test1'].values
x = np.column_stack((x, df['Test2'].values))
y = df['Admin'].values
row_num = y.shape[0]
x = np.insert(x, 0, values = np.ones((1, x.shape[0])), axis = 1)
'''y = y.reshape(len(y), 1)
y = np.tile(y, x.shape[1])'''
# h(x)
h(x) = 1 / (1 + np.e** (-N))
N = np.dot(x, theta.T)
# sum
sum = np.dot((h(x) - y).T, x)
theta = theta - alpha / m * sum
# jtheta
one = np.ones((1,row_num))
sum_part = y * np.log(h(x)) + (one - y) * np.log(one - h(x))
j = - 1 / row_num * sum_part
