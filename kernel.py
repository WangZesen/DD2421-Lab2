import math

def linear(x, y):
	v = 0
	for i in range(len(x)):
		v = v + x[i] * y[i];
	return (v + 1)


def poly(x, y, p):
	v = 0
	for i in range(len(x)):
		v = v + x[i] * y[i]
	return (v + 1) ** p

def radial(x, y, sig):
	v = 0
	for i in range(len(x)):
		v = v + (x[i] - y[i]) ** 2
	return math.e ** (- v / 2 / sig ** 2)

def sigmoid(x, y, k, delta):
	v = 0
	for i in range(len(x)):
		v = v + x[i] * y[i]
	return math.tanh(k * v - delta)
