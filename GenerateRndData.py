# -*- coding: utf-8 -*-
"""
Created on Mar  05 2016

@author: Tecnicamente
This module will contains functions for generate random data to test
the format is CSV

29/03/2016
Version 1.0
"""
import numpy as np
import csv
from myfile import CreaFileOutput


AvailableWorkingDays		= 220	# available working days in one year
CostPerHour					= 80 	# €/h

RevenueFactor				= 0.2	# %
PertubationForRevenueFactor	= 0.5	# %

NumberOfResouces			= 4		# available developers

TimeAvailabilityForResource	= 8		# 8h/day

MinimunNumberOfMachines		= 1
MaximumNumberOfMachines 	= 100

MinimumTurnoverPerMachine	= 3000	# €
MaximimTurnoverPerMachine	= 30000	# €

MinimumTimeForDevelopment	= 150	# h
MaximumTimeForDevelopment	= 500	# h

MaximumProjectsRequests		= 20	# Projects request per year

OutputFile = "ListOfProjects.csv"
OutputFile = CreaFileOutput(OutputFile)

FirstRow = "Request Number","Day when required","Development Time (h)","Development costs (€)","Machines","Turnover (€)","Revenue (€)"

writer = csv.writer(OutputFile)
writer.writerow(FirstRow)

ListOfRows = []

# radom data set creation
for i in range(MaximumProjectsRequests):
	row=[]
	row.append(i)																						# 0	Generate the item number
	row.append(np.random.randint(0,AvailableWorkingDays))												# 1	Generate the day of the year when the project request is communicated
	row.append(np.random.randint(MinimumTimeForDevelopment,MaximumTimeForDevelopment))					# 2 Generate the required time for the development
	row.append(row[2]*CostPerHour)																		# 3
	row.append(np.random.randint(MinimunNumberOfMachines,MaximumNumberOfMachines))						# 4
	row.append(row[4] * np.random.randint(MinimumTurnoverPerMachine,MaximimTurnoverPerMachine))			# 5
	row.append(row[5] * RevenueFactor * (np.random.randint(0,PertubationForRevenueFactor * 100)/100.))	# 6
	ListOfRows.append(row)

# sort of random data set in function of the value "Day when required"
buffer = []
for i in range(MaximumProjectsRequests):
	for j in range(i,MaximumProjectsRequests - 1):
		if ListOfRows[i][1] > ListOfRows[j][1]:
			buffer = ListOfRows[i]
			ListOfRows[i] = ListOfRows[j]
			ListOfRows[j] = buffer	

for i in range(MaximumProjectsRequests):
	writer.writerow(ListOfRows[i])

OutputFile.close
	
	