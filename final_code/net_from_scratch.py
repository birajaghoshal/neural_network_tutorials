import autograd.numpy as np
from autograd import elementwise_grad
from autograd import grad
import matplotlib.pyplot as plt

def objective(a):
	return 1/(1 + np.exp(a))

x = np.array([[1,1,0]
		,[1,0,0]
		,[1,1,1]
		,[0,1,1]])
y = np.array([[0,0,1,1]]).T
learning_rate = 1

np.random.seed(1)
#create weight vectors with average 0
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,4)) - 1
syn2 = 2*np.random.random((4,1)) - 1

# Set up figure.
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, frameon=False)
plt.ion()
plt.show()
count = 0

for iter in xrange(60000):

	l0 = x
	l1 = objective(np.dot(l0,syn0))
	l2 = objective(np.dot(l1,syn1))
	l3 = objective(np.dot(l2,syn2))

	objective_deriv = elementwise_grad(objective)

	delta_output = y - l3

	delta_l3 = delta_output*objective_deriv(l3)
	l2_error = np.dot(delta_l3, syn2.T)	#produces a 4x4 matrix

	delta_l2 = l2_error*objective_deriv(l2)
	l1_error = np.dot(delta_l2, syn1.T)

	delta_l1 = l1_error*objective_deriv(l1)

	syn2 += learning_rate*l2.T.dot(delta_l3)
	syn1 += learning_rate*l1.T.dot(delta_l2)
	syn0 += learning_rate*l0.T.dot(delta_l1)

	#plot
	count = count + 1
	ax.plot(delta_output)
	plt.draw()
	plt.pause(1.0/100000000.0)
