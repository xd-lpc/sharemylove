#create a mapping of status to abbreviation
states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'California':'NY',
    'Michigan':'MI'
}

#create a basic set of status and some cities in them

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#add more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities

print('-' * 20)
print("NY state has: ",cities['NY'])
print('OR state has: ', cities['OR'])


#print out some state
print('-' * 20)
print("Michigan's abbreviation is: ",states['Michigan'])

#print every abbreviation
print('-' * 20)
for state,abbrev in states.items():
    print("%s is abbreviated %s" %(state,abbrev))

#print every city in state
print('-' * 20)
for abbrev,city in cities.items():
    print("%s has the city %s" %(abbrev,city))

#now do both at the same time
print('-' * 20)
for state,abbrev in states.items():
    print("%s is abbreviated %s, and has city %s" %(state,abbrev,cities[abbrev]))

state = states.get('Texas',None)
if not state:
    print("sorry no Texas")

