## Output frequencies, as well as creates and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson
## Make sure your plots have names that are reasonably descriptive.

import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

testlist = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(testlist)
# Print data points
print c

# calculate the number of instances in the list
count_sum = sum(c.values())

# Print frequencies of data
for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)


# Boxplot of data
plt.boxplot(testlist)
plt.title('boxplot')
plt.ylabel('values')
plt.savefig("boxplot.png")
plt.show()

# Histogram of data
plt.hist(testlist, histtype='bar')
plt.title('histogram')
plt.xlabel('frequency')
plt.ylabel('values')
plt.savefig("histogram.png")
plt.show()

# QQ Plot
plt.figure()  
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.show()
