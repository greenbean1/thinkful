# Multivariate analysis of loansData

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

loansData = pd.read_csv('loansData_clean.csv')

income = loansData['Monthly.Income']
intrate = loansData['Interest.Rate']

f = smf.ols(formula='intrate ~ income', data=loansData).fit()
f.summary()

homeown = loansData['Home.Ownership']
loansData['homeownership'] = loansData['Home.Ownership']	# Needed just for python syntax
loansData['home'] = pd.Categorical(loansData.'Home.Ownership').labels

f2 = smf.ols(formula='intrate ~ income + homeown', data=loansData).fit()
f2.summary()

f3 = smf.ols(formula='intrate ~ income * homeown', data=loansData).fit()
f3.summary()
