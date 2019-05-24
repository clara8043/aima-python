# a1.py

from search import *
import numpy as np
import random
# ...
#Question 1. make Random 8 Puzzle and display the state
def make_rand_8puzzle(): # makes random 8 puzzle
	while True:
		lst=tuple(np.random.choice(range(9), 9, replace=False))
		p=EightPuzzle(lst)
		if p.check_solvability(p.initial): #return the puzzle only if solvable
			break
	return p

#Question 1. prints a readable representation of an eightpuzzle
def display(state): 
	s1 =""
	s2 = ""
	s3=""
	for i in range(9):
		if(i <= 2):

			if(state[i] != 0):
				s1 += str(state[i]) + " "
			else:
				s1 += "* "
		elif(i>2 and i <=5 ):
			if(state[i] != 0):
				s2 += str(state[i]) + " "
			else:
				s2 += "* "
		else:
			if(state[i] != 0):
				s3 += str(state[i]) + " "
			else:
				s3 += "* "
	print(s1 + "\n" + s2 + "\n" + s3)
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
        	#
        	return (count,node.depth)
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
   a1=astar_search1(p,h1)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h1(in seconds): {elapsed_time}')
   print('The total number of nodes removed : '+str(a1[0]))
   print('The length of the solution : '+str(a1[1])+'\n')

   #Runs Manhattan Function for astar search and records time
   start_time = time.time()
   a1=astar_search1(p,h2)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h2 (in seconds): {elapsed_time}')
   print('The total number of nodes removed : '+str(a1[0]))
   print('The length of the solution : '+str(a1[1])+'\n')
   
   #Runs Max of h1 and h2 for astar search and records time
   start_time = time.time()
   a1=astar_search1(p,h3)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h3(in seconds): {elapsed_time}')
   print('The total number of nodes removed : '+str(a1[0]))
   print('The length of the solution : '+str(a1[1])+'\n')
   return()
#This creates ten random Eight Puzzles and runs astar on each of them
def create():
	a=[0]*10
	for i in range (10):
		p=make_rand_8puzzle()
		a[i]=p
		f(p)
	return()
 create()


#Q3.Implement YPuzzle class
class YPuzzle(Problem):

    """ The problem of sliding tiles numbered from 1 to 8 on a Y puzzle,
    where one of the squares is a blank. A state is represented as a tuple of length 9,
    where element at index i represents the tile number  at index i (0 if it's an empty square) """
 
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)
    
    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)
    #Modified the possible actions from 8puzzle class
    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT','UP2','DOWN2']       
        index_blank_square = self.find_blank_square(state)

        if index_blank_square==0:
        	possible_actions = ['DOWN2']
        elif index_blank_square==1:
        	possible_actions = ['DOWN']
        elif index_blank_square==2:
        	possible_actions = ['DOWN','UP2','RIGHT']
        elif index_blank_square==3:
        	possible_actions = ['DOWN','RIGHT','LEFT']
        elif index_blank_square==4:
        	possible_actions = ['DOWN','UP','LEFT']
        elif index_blank_square==5:
        	possible_actions = ['UP','RIGHT']
        elif index_blank_square==6:
        	possible_actions = ['DOWN2','UP','LEFT','RIGHT']
        elif index_blank_square==7:
        	possible_actions = ['UP','LEFT']	
        elif index_blank_square==8:
        	possible_actions = ['UP2']

        return possible_actions
    #Modified results from 8puzzle class
    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        strgs = list(state)

        delta = {'UP':-3, 'DOWN':3, 'LEFT':-1, 'RIGHT':1, 'DOWN2':2,'UP2':-2}
        neighbor = blank + delta[action]
        strgs[blank], strgs[neighbor] = strgs[neighbor], strgs[blank]

        return tuple(strgs)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))

#Implement making random y puzzle function
#Created Puzzles that are solvable instead of creating another solvability function
def make_rand_ypuzzle():

	initpuzzle = (1,2,3,4,5,6,7,8,0)
	randPuzzle=YPuzzle(initpuzzle)
	for i in range(random.randint(0,50000)):
		direction = randPuzzle.actions(randPuzzle.initial)
		actionNumber = random.randint(0,len(direction)-1)
		nState = randPuzzle.result(randPuzzle.initial,direction[actionNumber])
		randPuzzle = YPuzzle(nState)
	return randPuzzle


#Function to display current state of ypuzzle
def displayY(state): 
	s1 =""
	s2 = ""
	s3 = ""
	s4 = ""
	strgs = ['']*9
	for i in range(9):
		if i==state.index(0):
			strgs[i]='*'
		else:
			strgs[i]=str(state[i])
	for i in range(9):
		if i<2:
			s1+=strgs[i]+"   "
		elif i>=2 and i<5:
			s2+=strgs[i]+" "
		elif i>=5 and i<8:
			s3+=strgs[i]+" "
		else:
			s4+="  " +strgs[i]
	print(s1 + "\n" + s2 + "\n" + s3 + "\n" + s4)
	return()



#Create a Manhattan function for YPuzzle using modified row/column function from above
def Yrow(x):
	p=0
	if x<=2 :
		p=1
	elif x<=5 :
		p=2
	elif x<=8 :
		p=3
	else : 
		p=4
	return p

def Ycol(x):
	p=0
	if x==1 or x==3 or x==6:
		p=1
	elif x==4 or x==7 or x==0:
		p=2
	else:
		p=3
	return p
def h4(puzzle):
	a=[0]*12
	x=0
	b=(1,2,3,4,5,6,7,8,0)
	for i in range(9):
		if puzzle.state[i]!=b[i] and puzzle.state[i]!=0:
			a[i]=abs(Yrow(puzzle.state[i])-Ycol(i+1))+abs(Yrow(puzzle.state[i])-Ycol(i+1))
	#The two cases where the row/column function does not work is when 1 is in the place of 2 and vice versa
	if puzzle.state[0]==b[1]:
		a[0]+=2
	if puzzle.state[1]==b[2]:
		a[1]+=2
	return sum(a)

#Function that uses maximum of Misplaced tiles and Manhattan function
def h5(puzzle):
	if h1(puzzle)>h4(puzzle):
		return h1(puzzle)
	else:
		return h4(puzzle)

#This creates twenty random Y Puzzles and runs astar on each of them


def fy(p):
   start_time = time.time()
   # ... do something ...
   #Runs Misplaced Tile Function astar search and records time
   a1=astar_search1(p,h1)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h1(in seconds): {elapsed_time}')
   print('The total number of nodes removed : '+str(a1[0]))
   print('The length of the solution : '+str(a1[1])+'\n')

   #Runs Manhattan Function for astar search and records time
   start_time = time.time()
   a1=astar_search1(p,h4)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h4 (in seconds): {elapsed_time}')
   print('The total number of nodes removed : '+str(a1[0]))
   print('The length of the solution : '+str(a1[1])+'\n')
   
   #Runs Max of h1 and h4 for astar search and records time
   start_time = time.time()
   a1=astar_search1(p,h5)
   elapsed_time = time.time() - start_time
   print(f'elapsed time for h5(in seconds): {elapsed_time}')
   print('The total number of nodes removed : '+str(a1[0]))
   print('The length of the solution : '+str(a1[1])+'\n')
   return()

def ycreate():
	a=[0]*20
	for i in range (20):
		p=make_rand_ypuzzle()
		a[i]=p
		fy(p)
	return()

ycreate()
