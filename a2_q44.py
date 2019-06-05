from a2_q2 import *
import time #to find the elapsed time
import openpyxl 
#USED MODIFIED VERSION OF CSP : CREATED AN INHERITANCE OF CSP CALLED CSP_MOD IN a2_q2.py
#CREATED IN Q2 FILE BECAUSE OF EFFICIENCY OF USAGE
#CSP_MOD INCLUDES ONE MORE MEMBER self.unassigns TO COUNT THE UNASSIGNED CSP VARIABLES WHILE LOOKING FOR A SOLUTION
#THUS IT INCREMENTS IN FUNCTION unassign IN THE CLASS
#MapColoringCSP_MOD	ENSURES THAT WE USE THE ABOCE CSP_MOD FOR MAPC COLOURING

wb = openpyxl.Workbook()	# Create a workbook in which an excel sheet will be created
sheet = wb.active			# create an active sheet in workbook
sheet.title = "Assignment2_Question3" # title of the sheet


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
#CREATE FIVE INSTANCES OF ABOVE q4 AND OUPTUTS THEM
def run_q4():
	for i in range(5):
		print('-------------',i+1,'th iteration--------------------------')
		q4(makegraphs())
		print('-------------------------------------------------------\n')


def insert_into_cell(r,c,val):
	""" Inserts val in the cell at row r and column c """
	c = sheet.cell(row=r,column=c)
	c.value = val

def q4_excel_sheet():
	print('!!!!!! BUILDING EXCEL SHEET .............\n')
	sRow = 1	# sheet row index (global var)
	sCol = 1	# sheet column index (global var)
	insert_into_cell(sRow,sCol,'Assignment 2: Question 3 Data')
	sRow+= 2
	for i in range(5):
		insert_into_cell(sRow,sCol,'ITERATION #'+str(i+1))
		sRow+=1
		insert_into_cell(sRow,sCol,'Friendship graph #')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of People/Nodes [n]')
		sCol+=1
		insert_into_cell(sRow,sCol,'Probability of Friendship [p]')
		sCol+=1
		insert_into_cell(sRow,sCol,'Time taken to solve Ice-breaker Problem [seconds]')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of Variables Assigned')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of Variables Unassigned')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of Team')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of Total Conflicts')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of Assigned Variables in Last Case')
		sCol+=1
		insert_into_cell(sRow,sCol,'Number of UnAssigned Variables in Last Case')		
		sRow+=1
		graphs = makegraphs()
		gNum = 1
		gProb = 0.1
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

			insert_into_cell(sRow,sCol,gNum)
			sCol+=1
			insert_into_cell(sRow,sCol,30)
			sCol+=1
			insert_into_cell(sRow,sCol,gProb)
			sCol+=1
			insert_into_cell(sRow,sCol,elapsed_time)
			sCol+=1
			insert_into_cell(sRow,sCol,a)
			sCol+=1
			insert_into_cell(sRow,sCol,ua)
			sCol+=1
			insert_into_cell(sRow,sCol,max(alist)+1)
			sCol+=1
			insert_into_cell(sRow,sCol,tc)
			sCol+=1
			insert_into_cell(sRow,sCol,last_a)
			sCol+=1
			insert_into_cell(sRow,sCol,last_ua)
			sCol=1
			sRow+=1
			gProb+=0.1
			gNum+=1
		sRow+=5
	wb.save('a2_q4.xlsx')
	print('DATA RECORDED IN "a2_q4.xlsx" IN THE ROOT DIRECTORY !!!!!!')

#run_q4()
q4_excel_sheet()