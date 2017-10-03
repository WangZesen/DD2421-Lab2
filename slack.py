import kernel
from cvxopt.solvers import qp
from cvxopt.base import matrix
import random, pylab, math, numpy

usedKernel = kernel.poly
dimen = 2


def buildP(data):
	length = len(data)
	p = [[0 for col in range(length)] for row in range(length)]
	for i in range(length):
		for j in range(length):
			p[i][j] = data[i][-1] * data[j][-1] * usedKernel(data[i][:-1], data[j][:-1], dimen)
	return p
	
def ind(datap, data):
	length = len(data)
	s = 0

	for i in range(length):
		v = usedKernel(datap, data[i][1][:-1], dimen)
		s = s + data[i][0] * data[i][1][-1] * v
	return s

random.seed(100)

classA = [(random.normalvariate(-1.5, 1) , random.normalvariate(0.5, 1), 1.0) for i in range (5)] + [(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range (5)]

classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-0.5 ,0.5), -1.0) for i in range (10)]

data = classA + classB
random.shuffle(data)

length = len(data)

q = [[-1.0  for i in range(length)]]

h = [[0.0 for i in range(2 * length)]]

slackValue = 0.5

for i in range(length):
	h[0][i + length] = slackValue

G = [[0.0 for col in range(2 * length)] for row in range(length)]



for i in range(length):
	G[i][i] = - 1.0
	G[i][i  + length] = 1.0

P = buildP(data)

print (len(P), len(P[0]))

r = qp(matrix(P), matrix(q), matrix(G), matrix(h))

alpha = list(r['x'])

#print (alpha)

points = []

for i in range(length):
	if alpha[i] > 0.00001:
		points.append((alpha[i], data[i]))
		
pylab.hold(True)
pylab.plot([p[0] for p in classA], [p[1] for p in classA], 'bo')
pylab.plot([p[0] for p in classB], [p[1] for p in classB], 'ro')
#pylab.show()

xrange=numpy.arange(-4, 4, 0.05)
yrange=numpy.arange(-4, 4, 0.05)

grid = matrix([[ind((x, y), points) for y in yrange] for x in xrange])

pylab.contour(xrange, yrange, grid, (-1.0, 0.0, 1.0), colors = ('red', 'black', 'blue'), linewidths = (1, 3, 1))

pylab.show()
