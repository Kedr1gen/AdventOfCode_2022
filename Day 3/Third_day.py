## Getting alphabet through string module

# import string
# lowercase_alphabets=list(string.ascii_lowercase)
# print(lowercase_alphabets)
# uppercase_alphabets=list(string.ascii_uppercase)
# print(uppercase_alphabets)
# alphabets=list(string.ascii_letters)
# print(alphabets)

totalPriority = 0
badgeTotalPriority = 0
lowerCaseAlpha = []
upperCaseAlpha = []
letter = []
numbers = []
workingGroup = []


## Get letter from their ASCII values
for i in range (97, 123):
	lowerCaseAlpha.append(chr(i))

for j in range (65, 91):
	upperCaseAlpha.append(chr(j))

letters = lowerCaseAlpha + upperCaseAlpha

for k in range (52):
	numbers.append(k+1)

## Generate dictionary
prioDictionary = dict.fromkeys(letters, 0)

prioDictionary = dict(zip(list(prioDictionary.keys()), numbers))

##### To the task!

f = open ("rucksacks.txt")

listOfLines = f.readlines()

## Strip items of "\n" as I have it as list now and it does not serve any purpose
for i in range(len(listOfLines)-1):
	listOfLines[i] = listOfLines[i][:-1]

## Part one solution
for line in listOfLines:
	lenghtOfCompartment = len(line)//2
	firstCompartment = line[:lenghtOfCompartment]
	secondCompartment = line[lenghtOfCompartment:]
	
	for item in firstCompartment:
		if item in secondCompartment:
			## I need to generate directory with item:priority pairs, check it here and save priority
			totalPriority += prioDictionary[item]
			break

#Part two solution
for i in range(0, len(listOfLines), 3):
	
	workingGroup = []
	#workingGroup.append(listOfLines[i:i+3]) #This produces nested list, at this point I do not want that
	firstRucksack = listOfLines[i]
	secondRucksack = listOfLines[i+1]
	thirdRucksack = listOfLines[i+2]

	for item in firstRucksack:
		if item in secondRucksack and item in thirdRucksack:
			badgeTotalPriority += prioDictionary[item]
			break

	
print (badgeTotalPriority)

f.close()