from a2_q2 import *
import time #to find the elapsed time

#For Q4, We use the child class of CSP which is CSP_MOD by importing this class from a2_q3 file
#We use the min_conflicts function to approximate the number of groups we can make. This function takes input CSP_MOD


#q4 takes a set of five graphs as input. Then, 
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
			#check if the solution satisfies the constraints and the min_conflicts hill climbing algorithm has fully iterated with a solution
			if check_teams(graphs[i],mincon)==True and mincon!=None:
				break
		elapsed_time = time.time() - start_time

		#calculate the number of teams that people are divided into
		#allocate all the values from mincon(the solution dictionary) to an empty array in order to use max function 
		alist = [0] * len(mincon) #create empty array of size of the min_conflicts
		for k in range(len(mincon)):
			alist[k]=mincon[k] #The maximum number of this array is the last group number (group number starts from zero)

		#print statistics
		print('==========q4========= p== 0.',i+1,'=============================')
		print('The number of teams people are divided into : ',max(alist)+1) #added 1 since group name starts from zero
		print(f'elapsed time for exact minimum number(in seconds): {elapsed_time}')
		print('The count of number of times CSP variables were assigned : ',a)
		print('The count of number of times CSP variables were unassigned : ',ua)
		print('==================================================================\n')

#makegraphs is a function that produces five random graphs with n=100 and different p values from 0.1 to 0.5
def makegraphs():
	graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3), rand_graph(100, 0.4), rand_graph(100, 0.5)]
	return graphs

#run q4 function above five times
def run_q4():
	for i in range(5):
		print('-------------',i+1,'th iteration--------------------------')
		q4(makegraphs())
		print('-------------------------------------------------------\n')

run_q4()
