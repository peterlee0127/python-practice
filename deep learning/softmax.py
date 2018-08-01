import numpy as np

def pre_softmax(a):
 exp_a = np.exp(a)
 sum_exp_a = np.sum(exp_a)
 y = exp_a / sum_exp_a
 return y

def softmax(a):
# prevent overflow
 c = np.max(a)
 exp_a = np.exp(a-c)
 sum_exp_a = np.sum(exp_a)
 y = exp_a / sum_exp_a
 return y

a = np.array([15,14,12])
print(pre_softmax(a))
print(softmax(a))



