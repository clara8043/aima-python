from a2_q1 import *

def check_teams(graph, csp_sol):
	if csp_sol==None:
		return False
	for i in range(len(graph)-1) : 
		for j in range(i+1,len(graph)):
			if (csp_sol[i]==csp_sol[j]) and (j in graph[i]):
				return False
	return True

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

#MODIFIED version of textbook MapColouringCSP to ensure we use the CSP_MOD instead of CSP
def MapColoringCSP_MOD(colors, neighbors):
	"""Make a CSP for the problem of coloring a map with different colors
	for any two adjacent regions. Arguments are a list of colors, and a
	dict of {region: [neighbor,...]} entries. This dict may also be
	specified as a string of the form defined by parse_neighbors."""
	if isinstance(neighbors, str):
		neighbors = parse_neighbors(neighbors)
	return CSP_MOD(list(neighbors.keys()), UniversalDict(colors), neighbors,
			   different_values_constraint)


# Test check_teams
# X = {0:0, 1:1, 2:1, 3:0}
# g = {0: [1, 2], 1: [0], 2: [0], 3: []} 
# k = check_teams(g,X)
# print(k)

# X = {0:0, 1:1, 2:3, 3:3}
# g = {0: [], 1: [], 2: [3], 3: [2]} 
# k = check_teams(g,X)
# print(k)
