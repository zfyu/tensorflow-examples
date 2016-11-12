x_old = 0
x_new = 6 # the algorithm starts at x=6
gamma = 0.01 #step size
precision = 0.00001

def df(x):
	y = 4*x**3-9*x**2
	return y
while abs(x_new-x_old)>precision:
	x_old = x_new
	x_new += -gamma*df(x_old)
print("the local minimum occurs at",x_new)
