from a2_q2 import *
import time #to find the elapsed time

#USED MODIFIED VERSION OF CSP : CREATED AN INHERITANCE OF CSP CALLED CSP_MOD IN a2_q2.py
#CREATED IN Q2 FILE BECAUSE OF EFFICIENCY OF USAGE
#CSP_MOD INCLUDES self.unassigns TO COUNT THE UNASSIGNED CSP VARIABLES WHILE LOOKING FOR A SOLUTION
#CSP_MOD INCLUDES self.totcon TO COUNT THE NUMBER OF CONLFICTS WHILE GETTING TO THE SOLUTION

#MapColoringCSP_MOD	ENSURES THAT WE USE THE ABOCE CSP_MOD FOR MAPC COLOURING

#We use the min_conflicts function to approximate the number of groups we can make. This function takes input CSP_MOD


def q4(graphs):

	for i in range(5):
		start_time = time.time()
		# ... do something ...
		a=0 #counter for times CSP variables were assigned

		#ua is a counter for times CSP variables were assigned, however it is not necessary and is always 0 in this case
		#since min_conflicts does not unassign CSP variables in the process
		ua=0 #counter for times CSP variables were unassigned

		tc=0 #counter for total conflict cases
		last_ua=0 #initialize the number of our last case of unassigned variables
		last_a=0 #initialize the number of our last case of assigned variables
		for j in range(100):
			mccsp=MapColoringCSP_MOD(range(0,j+1),graphs[i])
			#As the max_steps value input goes up, the elapsed time for running CSP for each graphs increases. 
			#If max_steps=100000 like the original value in the textbook code, elapsed time becomes around x200 longer than max_steps=1000
			#However, the larger max_steps are, the closer we get to the exact minimum number of groups
			mincon=min_conflicts(mccsp,max_steps=1500)
			a+=mccsp.nassigns
			ua+=mccsp.unassigns
			tc+=mccsp.totcon
			#check if the solution satisfies the constraints and the min_conflicts hill climbing algorithm has fully iterated with a solution
			if check_teams(graphs[i],mincon)==True and mincon!=None:
				last_ua=mccsp.unassigns
				last_a=mccsp.nassigns
				break
		elapsed_time = time.time() - start_time

		#calculate the number of teams that people are divided into
		#allocate all the values from mincon(the solution dictionary) to an empty array in order to use max function 
		alist = [0] * len(mincon) #create empty array of size of the min_conflicts
		for k in range(len(mincon)):
			alist[k]=mincon[k] #The maximum number of this array is the last group number (group number starts from zero)

		#print statistics
		print('==========q4========= p== 0.',i+1,'=============================')
		print('The number of teams that people are divided into : ',max(alist)+1) #added 1 since group name starts from zero
		print(f'elapsed time for exact minimum number(in seconds): {elapsed_time}')
		print('The total number of times CSP variables were assigned : ',a)
		print('The total number of times CSP variables were unassigned : ',ua)
		print('The total number of times CSP variables had conflicts : ',tc)
		print('The number of assigned variables in our last case : ',last_a)		
		print('The number of unassigned variables in our last case : ',last_ua)								
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
