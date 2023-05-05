"""
Simon Podsiadlik
Converting the Current-Time Relationship to a value for Capacity
"""
import numpy as np

try:
   #Define data arrays
    time_data = []
    current_data = []

    #Read in the data
    lines = np.loadtxt('Current_Values.txt', delimiter = ',', skiprows=2)
    for line in lines:
        time_data.append(line[0]) 		#First item in the row is the time
        current_data.append(line[1])	        #Second item in the row is the current

    charge = 0
    n = 0
    #There are 150 Values in the array
    while n < 149:

        current = current_data[n+1]

        time1 = time_data[n]
        time2 = time_data[n+1]

        charge += ((current)*(time2 - time1))
        n += 1

    print(charge, "is the battery's capactiy in Coloumbs!")
    print((charge/3.6), "is the battery's capacity in milliAmp-hours!")


except KeyboardInterrupt:
    print("Checkmate!")
