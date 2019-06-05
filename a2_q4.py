from a2_q3 import *

#For Q4, We use the child class of CSP which is CSP_MOD by importing this class from a2_q3 file
#We use the min_conflicts function to approximate the number of groups we can make. This function takes input CSP_MOD

#makegraphs is to produce five random graphs with n=100 and different p values from 0.1 to 0.5
def makegraphs():
	graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3), rand_graph(100, 0.4), rand_graph(100, 0.5)]
	return graphs

#q4 takes a set of five graphs as input. Then, use min
def q4(graphs):

	for i in range(5):
		start_time = time.time()
		# ... do something ...
		a=0 #counter for times CSP variables were assigned
		#ua is a counter for times CSP variables were assigned, however it is not necessary and is always 0 in this case
		#since min_conflicts does not unassign CSP variables in the process
		ua=0 #counter for times CSP variables were unassigned
		for j in range(100):
			mccsp=MapColoringCSP_MOD(range(0,j+1),graphs[i])
			#As the max_steps value input goes up, the elapsed time for running CSP for each graphs increases. 
			#If max_steps=100000 like the original value in the textbook code, elapsed time becomes around x200 longer than max_steps=1000
			#However, the larger max_steps are, the closer we get to the exact minimum number of groups
			mincon=min_conflicts(mccsp,max_steps=1500)
			a+=mccsp.nassigns
			ua+=mccsp.unassigns
			if check_teams(graphs[i],mincon)==True and mincon!=None:
				break
		elapsed_time = time.time() - start_time

		#calculate the number of teams that people are divided into
		alist = [0] * len(mincon)
		for k in range(len(mincon)):
			alist[k]=mincon[k]
		print('====q4--==========================================================')
		print('The number of teams people are divided into : ',max(alist)+1)
		print(f'elapsed time for exact minimum number(in seconds): {elapsed_time}')
		print('The count of number of times CSP variables were assigned : ',a)
		print('The count of number of times CSP variables were unassigned : ',ua)
		print('==================================================================\n')

def q41(graphs):

	for i in range(5):
		start_time = time.time()
		# ... do something ...
		a=0 #counter for times CSP variables were assigned
		ua=0 #counter for times CSP variables were unassigned
		for j in range(100):
			mccsp=MapColoringCSP_MOD(range(0,100),graphs[i])
			mincon=min_conflicts_MOD(mccsp)
			a+=mccsp.nassigns
			ua+=mccsp.unassigns
			if check_teams(graphs[i],mincon)==True and mincon!=None:
				break
		elapsed_time = time.time() - start_time

		#calculate the number of teams that people are divided into
		alist = [0] * len(mincon)
		for k in range(len(mincon)):
			alist[k]=mincon[k]
		print('====q4-1==========================================================')
		print('The number of teams people are divided into : ',max(alist)+1)
		print(f'elapsed time for exact minimum number(in seconds): {elapsed_time}')
		print('The count of number of times CSP variables were assigned : ',a)
		print('The count of number of times CSP variables were unassigned : ',ua)
		print('==================================================================\n')



def run_q4():
	for i in range(5):
		g=makegraphs()
		q4(g)
		#q41(g)

run_q4()
