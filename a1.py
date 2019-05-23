# a1.py

from search import *
import numpy as np
# ...
#Question 1. make Random 8 Puzzle and display the state
def make_rand_8puzzle(): # makes random 8 puzzle
	while True:
		lst=tuple(np.random.choice(range(9), 9, replace=False))
		p=EightPuzzle(lst)
		if p.check_solvability(p.initial): #return the puzzle only if solvable
			break
	# s = (5,1,6,2,0,3,7,4,8)
	# p = EightPuzzle(s)
	return p

#Question 1. prints a readable representation of an eightpuzzle
def display(state): 
	r1 =""
	r2 = ""
	r3=""
	for i in range(9):
		if(i <= 2):

			if(state[i] != 0):
				r1 += str(state[i]) + " "
			else:
				r1 += "* "
		elif(i>2 and i <=5 ):
			if(state[i] != 0):
				r2 += str(state[i]) + " "
			else:
				r2 += "* "
		else:
			if(state[i] != 0):
				r3 += str(state[i]) + " "
			else:
				r3 += "* "
	print(r1 + "\n" + r2 + "\n" + r3)
	return()
#Question2. create Misplaced tiles puzzle
def h1(puzzle):
	x=0
	for i in range(9):
		if puzzle.state[i]!= i+1 and puzzle.state[i]!=0:
			x+=1
	return x
#The below rowx and columnx is used to find the coordinates of 
#the each element in the (current) puzzle
def rowx(x):
	p=int((x-1)/3)
	return p

def columnx(x):
	if x%3!=0:
		p=x%3
	else:
		p=3
	return p
#Question2.This manhattan function calculates the differences in the 
#rows and columns of the goal state and the current state
def h2(puzzle):
	a=[0]*9
	x=0
	for i in range(9):
		if puzzle.state[i]!=i+1 and puzzle.state[i]!=0:
			a[i]=abs(rowx(puzzle.state[i])-rowx(i+1))+abs(columnx(puzzle.state[i])-columnx(i+1))
	return sum(a)
#Question2.
#This function is a function that calculate the max of the misplaced tile heuristic and the Manhattan distance heuristic
def h3(puzzle):
	if h1(puzzle)>h2(puzzle):
		return h1(puzzle)
	else:
		return h2(puzzle)
#Question2
#The two functions below is from search.py modified to get the number of nodes removed
def astar_search1(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search1(problem, lambda n: n.path_cost + h(n))

def best_first_graph_search1(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    count=0
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        count+=1
        if problem.goal_test(node.state):
        	#The print function below outputs the total number of nodes removed from frontier
        	#This prints while running astar_search1 below 
        	print('the total number of nodes that were removed from the frontier : '+str(count))
        	return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None
#Question2.
#This is the time function for functions h1,h2,h3 and prints the length of the solution
import time
def f(p):
   start_time = time.time()

   # ... do something ...
   #Runs Misplaced Tile Function astar search and records time
   astar_search1(p,h1)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h1(in seconds): {elapsed_time}')

   #Runs Manhattan Function for astar search and records time
   astar_search1(p,h2)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h2 (in seconds): {elapsed_time}')
   
   #Runs Max of h1 and h2 for astar search and records time
   astar_search1(p,h3)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h3(in seconds): {elapsed_time}')
   #prints the length of the solution
   print('Length of the solution is :'+len(p.solution()))
   return()
#This creates ten random Eight Puzzles and runs astar on each of them
def create():
	a=[0]*9
	for i in range (10):
		p=make_rand_8puzzle()
		a[i]=p
		f(p)
	return()
create()


#Q3.Implement YPuzzle class
class YPuzzle(Problem):

    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank. A state is represented as a tuple of length 9,
    where element at index i represents the tile number  at index i (0 if it's an empty square) """
 
    def __init__(self, initial, goal=(1,-1, 2, 3, 4, 5, 6, 7, 8,-1, 0,-1)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)
    
    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)
    
    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']       
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP':-3, 'DOWN':3, 'LEFT':-1, 'RIGHT':1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j]!= 0:
                    inversion += 1
        
        return inversion % 2 == 0
    
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))
