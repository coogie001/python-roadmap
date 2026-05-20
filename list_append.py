cities=['bristol', 'birmingham', 'manchester', 'utah', 'southampton']
cities2=["memphis","orlando","north carolina"]
var_1=cities+cities2
print(var_1)
print(" ")
var_1.append("south carolina")
print(var_1)
print(" ")
#extend
cities.extend(cities2)
print(cities)
print(" ")
cities3=["mongolia","buenos aires","mexico"]
cities2.extend(cities3)
print(cities2)
print(" ")
cities.append("south carolina")
print(cities)