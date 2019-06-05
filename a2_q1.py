import random #From python standard library
from csp import *

#This function takes 
def rand_graph(n,p):
	g=dict()
	for i in range(n):
		g.setdefault(i,[])
	for j in range(n-1):
		for k in range(j+1,n):
			r=random.randint(0,5500)/5500
			if r<=p:
				g[k].append(j)
				g[j].append(k)
	return g;

