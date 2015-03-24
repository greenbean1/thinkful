 Print out the cities with the July being the warmest month

Connect to the database
Create the cities and weather tables (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)
Insert data into the two tables
Join the data together
Load into a pandas DataFrame
Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."


import sqlite3 as lite
import pandas as pd

cities =(
		('New York City', 'NY'),
    	('Boston', 'MA'),
    	('Chicago', 'IL'),
    	('Miami', 'FL'),
    	('Dallas', 'TX'),
    	('Seattle', 'WA'),
    	('Portland', 'OR'),
    	('San Francisco', 'CA'),
    	('Los Angeles', 'CA'),
    	('Las Vegas', 'NV'),
    	('Atlanta', 'GA')
    )

weather =(
		('New York City', 2013, 'July', 'January', 62),
        ('Boston', 2013, 'July', 'January', 59),
        ('Chicago', 2013, 'July', 'January', 59),
        ('Miami', 2013, 'August', 'December', 84),
        ('Dallas', 2013, 'July', 'January', 77),
        ('Seattle', 2013, 'July', 'January', 61),
        ('Portland', 2013, 'July', 'December', 63),
        ('San Francisco', 2013, 'September', 'December', 64),
        ('Los Angeles', 2013, 'September', 'December', 75),
        ('Las Vegas', 2013, 'July', 'December', 70),
        ('Atlanta', 2013, 'July', 'January', 68)
    )


con = lite.connect('getting_started.db')

with con:
    cur = con.cursor()
    cur.execute("drop table if exists cities")
    cur.execute("create table cities (name text, state text)")
    cur.execute("drop table if exists weather")
    cur.execute("create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    ## SQL to join 
    sql_query = "select city, state from cities inner join weather on cities.name = weather.city where warm_month =?"
    cur.execute(sql_query, [("July")])
    rows = cur.fetchall()


#df = pd.DataFrame(rows)
df = pd.DataFrame(rows, columns = ['city','state'])
formatted_string = ''
for row in df.iterrows():
    #formatted_string += row['city'] + ', ' + row['state']
    #print formatted_string
    print row[1]
    print 'x'
    print row

placeholder = 'x'

print "The cities that are warmest in July are: %s" % placeholder
# str(df.[row][0]) + ', ' + str(df.[row][1])
con.close()