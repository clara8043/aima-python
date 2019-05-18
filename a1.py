# a1.py

from search import *

# ...

def make_rand_8puzzle():
	import numpy as np
	while True:
		lst=np.random.choice(range(9), 9, replace=False)
		p=EightPuzzle(lst)
		if p.check_solvability(p.initial)==True:
			break
	return p




def display(state):
	# ls=state
	# print(ls[0:3],'\n',ls[3:6],'\n',ls[6:9])
	# return ()
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


# p=  EightPuzzle((1,2,3,0,4,5,6,7,8),(1,2,3,4,5,6,7,8,9,0))
display(make_rand_8puzzle().initial)