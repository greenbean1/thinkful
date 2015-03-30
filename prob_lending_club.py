import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

#Create dataframe of loansData
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Print summary statistics of loansData dataframe
print loansData.describe()

#Clean data via removing rows with nulls values
loansData.dropna(inplace=True)

#Boxplot of 'Amount.Requested' column
loansData.boxplot(column='Amount.Requested')
plt.show()

#Histogram of 'Amount.Requested' column
loansData.hist(column='Amount.Requested')
plt.show()

#QQ Plot of 'Amount.Requested' column
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()