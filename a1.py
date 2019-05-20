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


def display(state): # dsplays the state of the current 8puzzle
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


# display(make_rand_8puzzle().initial)
p1=make_rand_8puzzle()
p2=make_rand_8puzzle()
p3=make_rand_8puzzle()
p4=make_rand_8puzzle()
p5=make_rand_8puzzle()
p6=make_rand_8puzzle()
p7=make_rand_8puzzle()
p8=make_rand_8puzzle()
p9=make_rand_8puzzle()
p0=make_rand_8puzzle()
def h1(puzzle):
	x=0
	# if puzzle.goal_test==True:
	# 	return x
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
#This manhattan function calculates the differences in the row and columns of the
#goal state and the current state
def h2(puzzle):
	a=[0]*9
	x=0
	for i in range(9):
		if puzzle.state[i]!=i+1 and puzzle.state[i]!=0:
			a[i]=abs(rowx(puzzle.state[i])-rowx(i+1))+abs(columnx(puzzle.state[i])-columnx(i+1))
	return sum(a)

display(p1.initial)
# print(mistile(p1))
# display(manhattan(p1))
astar_search(p1,h2)

