"""
Simon Podsiadlik
Plotting the collected Battery Discharge Data
"""

import matplotlib.pyplot as plt
import numpy as np

#Define data arrays
time_data = []
current_data = []


#Read in the data
lines = np.loadtxt('Current_Values.txt', delimiter = ',', skiprows=2)
for line in lines:
    time_data.append(line[0]/3600) 		#First item in the row is the time
    current_data.append(line[1])	        #Second item in the row is the current


#Make a plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#Make an x-y scatter plot
plt.scatter(time_data, current_data, color = 'blue')


#Label the axes
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Current (A)")
ax.set_title("9V Battery Current Drop")

plt.savefig('CurrentDischarge.png')
