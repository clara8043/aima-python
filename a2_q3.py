from a2_q2 import *
import time #to find the elapsed time

#USED MODIFIED VERSION OF CSP : CREATED AN INHERITANCE OF CSP CALLED CSP_MOD IN a2_q2.py
#CREATED IN Q2 FILE BECAUSE OF EFFICIENCY OF USAGE
#CSP_MOD INCLUDES ONE MORE MEMBER self.unassigns TO COUNT THE UNASSIGNED CSP VARIABLES WHILE LOOKING FOR A SOLUTION
#THUS IT INCREMENTS IN FUNCTION unassign IN THE CLASS
#MapColoringCSP_MOD	ENSURES THAT WE USE THE ABOCE CSP_MOD FOR MAPC COLOURING

def makegraphs():
	graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3), rand_graph(30, 0.4), rand_graph(30, 0.5)]
	return graphs

#Make five random graphs then for each graph, we run a backtracking_search using map colouring algorithm for each instances per person
def q3(graphs):
	for i in range(5):
		start_time = time.time()
		# ... do something ...
		a=0 #counter for times CSP variables were assigned
		ua=0 #counter for times CSP variables were unassigned
		tc=0 # counter for the number of each CSP variables having conflicts with each other
		last_ua=0 #initialize the number of our last case of unassigned variables
		last_a=0 #initialize the number of our last case of assigned variables		
		for j in range(30):
			mccsp=MapColoringCSP_MOD(range(0,j),graphs[i])

			#Use backtracking search for mccsp and input mrv and forward checking for more efficiency
			bcksrch=backtracking_search(mccsp,select_unassigned_variable=mrv, inference=forward_checking)
			a+=mccsp.nassigns #Add the  number of assigns to our total number of assigns in this graph
			ua+=mccsp.unassigns #Add the number of unassigned CSP Variable to our total number of unassigned variables in this graph
			tc+=mccsp.totcon #Adds the number of total conflicts of each CSP variable
			#Check if the constraints are satisfied when backtracking search algorithm has found a solution
			if check_teams(graphs[i],bcksrch)==True and bcksrch!=None:
				last_ua=mccsp.unassigns
				last_a=mccsp.nassigns				
				break	
		
		elapsed_time = time.time() - start_time

		#calculate the number of teams that people are divided into
		alist = [0] * len(bcksrch)
		for k in range(len(bcksrch)):
			alist[k]=bcksrch[k]
		print('==========q3========= p== 0.',i+1,'=============================')
		print('The number of teams that people are divided into : ',max(alist)+1)
		print(f'elapsed time for exact minimum number(in seconds): {elapsed_time}')
		print('The total number of times CSP variables were assigned : ',a)
		print('The total number of times CSP variables were unassigned : ',ua)
		print('The total number of times CSP variables had conflicts : ',tc)
		print('The number of assigned variables in our last case : ',last_a)		
		print('The number of unassigned variables in our last case : ',last_ua)			
		print('==============================================================\n')
		
#CREATE FIVE INSTANCES OF ABOVE Q3 AND OUPTUTS THEM
def run_q3():
	for i in range(5):
		print('-------------',i+1,'th iteration--------------------------')
		q3(makegraphs())
		print('-------------------------------------------------------\n')
run_q3()
