# Task is to determine the linear equation that fits the trend between FICO scores and interest rates

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Print summary statistics of loansData numeric columns
print loansData.describe()

# View first 5 rows of 'Loan.Length' column
loansData['Loan.Length'][0:5] # first 5 rows of Interest.Rate

# Clean 'Interest.Rate' column
cleaned_interest_rate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleaned_interest_rate

# Clean 'Loan.Length' column
cleaned_loan_length = loansData['Loan.Length'].map(lambda x: x.rstrip(' months'))
loansData['Loan.Length'] = cleaned_loan_length

# Clean 'FICO.Range' column
cleaned_fico_range = loansData['FICO.Range'].map(lambda x: int(x[:x.find('-')]))
loansData['FICO.Range'] = cleaned_fico_range

# Histogram of FICO Scores

plt.figure()
p = loansData['FICO.Range'].hist()
plt.show()

# Scatterplot matrix of loansData
plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()

# Linear Model: InterestRate = b + a1(FICOScore) + a2(LoanAmount)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Puts independent variables together in a matrix
x = np.column_stack([x1,x2])

# Create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# Print results
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared



# Scratch Work

#cleaned_fico_range = cleaned_fico_range.map(lambda x: [int(n) for n in x])

#cleaned_fico_range = cleaned_fico_range.map(lambda x: int(x))
#cleaned_fico_range = cleaned_fico_range.map(lambda x: x/1)
#type(cleaned_fico_range)
#
#loansData['FICO.Range'] = cleaned_fico_range
#
#loansData['Interest.Rate'][0:5].replace("%", "") # first 5 rows of Interest.Rate
#
#type(loansData['FICO.Range'][0:5].values[0])
#
# Practice cleaning with lambda function
#x = loansData['Interest.Rate'][0:5].values[1]
#f = lambda x: round(float(x.rstrip('%')) / 100, 4)
#cleaned_practice_fico_range = loansData['FICO.Range'].map(lambda x: x.rstrip(' months'))
#position = x.find('-')
#cleaned = int(x[:x.find('-')])
