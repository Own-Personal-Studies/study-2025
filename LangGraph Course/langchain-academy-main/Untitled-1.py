import numpy as np
n = 100
X = np.random.rand(n,2)
print(X.shape)
weights = np.array([2,3])
print(weights.shape)
bias = 5
e = X.dot(weights)
print(e)
print(e+5)
r = np.random.randn(n)
print(r)
print(e + 5 + r)
Y = X.dot(weights) + bias + r
