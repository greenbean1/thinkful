import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

a_rng = max(df['Alcohol']) - min(df['Alcohol'])
t_rng = max(df['Tobacco']) - min(df['Tobacco'])

a_avg = round(df['Alcohol'].mean(), 2)
t_avg = round(df['Tobacco'].mean(), 2)

a_var = round(df['Alcohol'].var(), 2)
t_var = round(df['Tobacco'].var(), 2)

a_std = round(df['Alcohol'].std(), 2)
t_std = round(df['Tobacco'].std(), 2)

a_med = round(df['Alcohol'].median(), 2)
t_med = round(df['Tobacco'].median(), 2)

a_mod = stats.mode(df['Alcohol'])[0][0]
t_mod = stats.mode(df['Tobacco'])[0][0]

print "The range for Alcohol is " + str(a_rng)
print "The range for Tobacco is " + str(t_rng)
print "The average for Alcohol is " + str(a_avg)
print "The average for Tobacco is " + str(t_avg)
print "The variance for Alcohol is " + str(a_var)
print "The variance for Tobacco is " + str(t_var)
print "The standard deviation for Alcohol is " + str(a_std)
print "The standard deviation for Tobacco is " + str(t_std)
print "The median for Alcohol is " + str(a_med)
print "The median for Tobacco is " + str(t_med)
print "The mode for Alcohol is " + str(a_mod)
print "The mode for Tobacco is " + str(t_mod)
