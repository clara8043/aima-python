from a2_q2 import *
import time #to find the elapsed time


#Child class of CSP that includes self.unassigns and iniitializes it to 0
class CSP_MOD(CSP):

	def __init__(self, variables, domains, neighbors, constraints):
		#MODIFIED to count number of unassignments
		self.unassigns = 0
		CSP.__init__(self, variables, domains, neighbors, constraints)
	def unassign(self, var, assignment):
		"""Remove {var: val} from assignment.
		DO NOT call this if you are changing a variable to a new value;
		just call assign for that."""
		if var in assignment:
			del assignment[var]
			self.unassigns+=1

#MODIFIED version of textbook MapColouringCSP to ensure we use the child class of CSP which is CSP_MOD
def MapColoringCSP_MOD(colors, neighbors):
	"""Make a CSP for the problem of coloring a map with different colors
	for any two adjacent regions. Arguments are a list of colors, and a
	dict of {region: [neighbor,...]} entries. This dict may also be
	specified as a string of the form defined by parse_neighbors."""
	if isinstance(neighbors, str):
		neighbors = parse_neighbors(neighbors)
	return CSP_MOD(list(neighbors.keys()), UniversalDict(colors), neighbors,
			   different_values_constraint)

graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
	rand_graph(30, 0.4), rand_graph(30, 0.5)]
#Make five random graphs then for each graph, we run a backtracking_search using map colouring algorithm for each instances per person
def q3():

	for i in range(5):
		start_time = time.time()
		# ... do something ...
		a=0 #counter for times CSP variables were assigned
		ua=0 #counter for times CSP variables were unassigned
		for j in range(30):
			mccsp=MapColoringCSP_MOD(range(0,j),graphs[i])

			#Use backtracking search for mccsp and input mrv and forward checking for more efficiency
			bcksrch=backtracking_search(mccsp,select_unassigned_variable=mrv, inference=forward_checking)
			a+=mccsp.nassigns #Add the  number of assigns to our total number of assigns in this graph
			ua+=mccsp.unassigns #Add the number of unassigned CSP Variable to our total number of unassigned variables in this graph

			#Check if the constraints are satisfied when backtracking search has finished
			# if bcksrch!=None and check_teams(graphs[i],bcksrch)==True:
			# 	break
			if check_teams(graphs[i],bcksrch)==True and bcksrch!=None:
				break	
		
		elapsed_time = time.time() - start_time

		#calculate the number of teams that people are divided into
		alist = [0] * len(bcksrch)
		for k in range(len(bcksrch)):
			alist[k]=bcksrch[k]
		print('==============================================================')
		print('The number of teams people are divided into : ',max(alist)+1)
		print(f'elapsed time for exact minimum number(in seconds): {elapsed_time}')
		print('The count of number of times CSP variables were assigned : ',a)
		print('The count of number of times CSP variables were unassigned : ',ua)
		print('==============================================================\n')

def run_q3():
	for i in range(5):
		q3()
#q3()
