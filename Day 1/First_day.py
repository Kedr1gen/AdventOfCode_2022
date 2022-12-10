f = open ("list.txt")

currentElf = 0 
listOfElves = []

for line in f:
	if line == "\n":
		listOfElves.append(currentElf)
		currentElf = 0
		continue
	line = line.strip()
	currentElf += int(line)
listOfElves.append(currentElf)

#print(listOfElves)
listOfElves.sort()
topThree = listOfElves[-3:]
sumTopThree = topThree[0] + topThree[1] + topThree[2]
print("Top three elves are carrying: %d" % sumTopThree)

f.close()