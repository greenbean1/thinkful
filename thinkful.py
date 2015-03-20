met = False
hour = 0
walker_a_speed = 2
walker_b_speed = 1
miles_from_london = 0
total_distance = 0

while not met:
	hour += 1
	total_distance = total_distance + walker_a_speed + walker_b_speed
	miles_from_london += 1
	if total_distance >= 102:
		met = True
		print('The walkers met', miles_from_london, 'miles from London and took', hour, 'hours')
	else:
		print('The walkers are still walking', miles_from_london, 'miles from London')

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    for line in inputFile:
        print line



import collections
population_dict = collections.defaultdict(list)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    population_dict['animals'] = ['cat','dog']
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
            population_dict[line[0]][0] += line[5]
            population_dict[line[0]][1] += line[6]
    print population_dict

with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,2010_population,2100_population\n')

    for k, v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
print outputFile