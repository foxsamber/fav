import math

def loss(theta,xi,yi):
	total = 0
	for index,i in enumerate(xi):
		total = theta[index]*i
	return total - yi

def final_loss(theta,xset,yset):
	sum = 0 
	for Xindex,Xm in enumerate(xset): 
		yi = yset[Xindex]
		hx = 0
		for index,t in enumerate(theta):
			hx =hx+ t*Xm[index]
		sum = sum + math.pow(hx-yi,2)
	return sum

def grediant(xset,yset,alpha,N,iter_num):
	theta = []
	for i in range(N):
		theta.append(0)
	#theta = [0,0.9]
	print final_loss(theta,xset,yset)
	for i in range(iter_num):
		for index in range(len(yset)):
			sub = loss(theta,xset[index],yset[index])
			for tindex,t in enumerate(theta):
				value=  sub*xset[index][tindex]
				theta[tindex] = theta[tindex] - alpha * value
			print 'loss',final_loss(theta,xset,yset)
			print theta
	
xset = [[1,1],[1,2],[1,3],[1,4],[1,5]]
yset = [1,2,3,4,5]
grediant(xset,yset,0.001,2,100)
