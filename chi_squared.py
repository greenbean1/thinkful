import pandas as pd
from scipy import stats
import collections
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Clean Data: Delete rows with null values
loansData.dropna(inplace=True)


freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Chi Square Test on whether 'Open CREDIT Lines' column has given frequencies
chi, p = stats.chisquare(freq.values())
print chi, p




## Additional info, counts, bar graph, etc practice

# Print summary statistics of data frame
print loansData.describe()

# calculate the number of instances in the list
count_sum = sum(freq.values())
print "There are " + str(count_sum) + " total open credit lines."

distinct_vals = 0
most_freq_val = 0
max_cnt = 0
# Print frequencies of data
for k,v in freq.iteritems():
  # Prints the frequency of each open credit line
  #print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)
  distinct_vals += 1
  if v > max_cnt:
  	max_cnt = v
  	most_freq_val = k

# Another way to count distinct credit lines
same_val = len(freq)

print "There are " + str(distinct_vals) + " unique open credit lines. This is the same as " + str(same_val)
print "The most frequent value is " + str(most_freq_val) + " and appears " + str(max_cnt) + " times."

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.xlabel('Open Credit Lines')
plt.ylabel('Count')
plt.show()