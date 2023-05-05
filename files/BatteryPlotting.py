"""
Simon Podsiadlik
2/1/2023
Plotting the collected Battery Discharge Data

"""

import matplotlib.pyplot as plt
import numpy as np

#Define data arrays
time_data = []
voltage_data = []


#Read in the data
lines = np.loadtxt('Test.txt', delimiter = ',')
for line in lines:
    time_data.append(line[0]/3600) 		#First item in the row is the time
    voltage_data.append(line[1])	#Second item in the row is the voltage
    


#Make a plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#Make an x-y scatter plot
plt.scatter(time_data, voltage_data, color = 'blue')


#Label the axes
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Voltage (V)")
ax.set_title("9V Battery Discharge Rate")

ax.text(0.4, 1.5, "Annotate the plot if needed.")
plt.savefig('FinalBatteryDischarge.png')