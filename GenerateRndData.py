# -*- coding: utf-8 -*-
"""
Created on Mar  05 2016

@author: Tecnicamente
This module will contains functions for generate random data to test
the format is CSV
"""
import numpy as np
import csv
from myfile import CreaFileOutput


NumberOfItemToGenerate		= 300
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

OutputFile = "ListOfProjects.csv"
OutputFile = CreaFileOutput(OutputFile)

FirstRow = "Request Number","Development Time (h)","Development costs (€)","Machines,Turnover (€)","Revenue (€)"

writer = csv.writer(OutputFile)

for i in range(NumberOfItemToGenerate):
	row=[]
	row.append(i)																					# 0
	row.append(np.random.randint(MinimumTimeForDevelopment,MaximumTimeForDevelopment))				# 1
	row.append(row[1]*CostPerHour)																	# 2
	row.append(np.random.randint(MinimunNumberOfMachines,MaximumNumberOfMachines))					# 3
	row.append(row[3] * np.random.randint(MinimumTurnoverPerMachine,MaximimTurnoverPerMachine))		# 4
	row.append(row[4] * RevenueFactor * (np.random.randint(0,PertubationForRevenueFactor * 100)/100.))# 5
	writer.writerow(row)

OutputFile.close
	
	