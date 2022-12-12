counter = 0

f = open("sections.txt")

listOfLines = f.readlines()

## Strip items of "\n" as I have it as list now and it does not serve any purpose
for i in range(len(listOfLines)-1):
	listOfLines[i] = listOfLines[i][:-1]

for line in listOfLines:

	line = line.split(",")
	line[0] = line[0].split("-")
	line[1] = line[1].split("-")

	a = int(line[0][0])
	b = int(line[0][1])
	c = int(line[1][0])
	d = int(line[1][1])



	## First part solution, counts complete overlaps
	# if a >= c and b <= d:
	# 	counter += 1
	# 	#print("Found in first check:")
	# 	#print(firstSection, secondSection)

	# elif c >= a and d <= b:
	# 	counter += 1
	# 	#print("Found in second check:")
	# 	#print(firstSection, secondSection)

	
	
	## Second part solution
	## Look at all cases whith NO overlap, skip them, thus count only overlaps, partial and full
	if a < c and b < c:
		continue
	elif a > d and b > d:
		continue

	elif c < a and d < a:
		continue
	elif c > b and d > b:
		continue

	counter += 1
	

print(counter)

f.close()