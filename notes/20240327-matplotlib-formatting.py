import numpy as np
import matplotlib.pyplot as plt

#%% - make random data for plotting purposes

mu, sigma = 0, 1
datanorm = np.random.normal(mu, sigma,100)
dataline = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

#%% - regular line (only y specified)

plt.subplots()
plt.plot([1, 2, 3, 4])
plt.ylabel('y values')

#%% - regular line with x and y specified

plt.subplots()
plt.plot([1, 2, 3, 4], [1, 16, 9, 4])

# QUESTION: which list is for x?
# QUESTION: which list is for y?

#%% - regular line with x and y specified

# TODO: write down a y list to obtain a straight line

plt.subplots()
plt.plot([3, 1, 4, 2] )

#%% - formatting

plt.subplots()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# QUESTION: What happened?

#%% - more formatting

plt.subplots()
plt.plot(dataline, 'r--')
plt.plot(dataline**2, 'bs')
plt.plot(dataline**3, 'g^')

# QUESTION: What happened?

#%% legends

plt.subplots()
plt.plot(dataline, 'r--')
plt.plot(dataline**2, 'bs')
plt.plot(dataline**3, 'g^')
plt.plot(-1*dataline**3, linewidth=2.0)

plt.legend(('values', 'values**2', 'values**3', '-1 * values**3'))

# QUESTION: What happened?

#%% error bars showing 95% CI or SEM

plt.subplots()
plt.bar([1,2,3], [10, 11, 12])
plt.errorbar([1], [10], yerr=[3])
plt.errorbar([2], [11], yerr=[50])

# TODO: add an error bar for the last x,y bar pair

#%% Preview of lab 8

# TODO: plot your data from lab 7 in several ways
# TODO: add error bars showing the SEM
# TODO: explain each plot and why it is informative or not for your data
# https://matplotlib.org/stable/gallery/index.html
