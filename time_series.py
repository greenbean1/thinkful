# Time-series analysis

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.graphics.tsaplots as sm


df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

# Try without to see if below plot still works
%pylab inline	

loan_count_summary[1:25].plot()

sm.plot_acf(loan_count_summary)
sm.plot_pacf(loan_count_summary)