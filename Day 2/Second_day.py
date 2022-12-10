def evaluateRound(enemy_choice, my_choice):
	if enemy_choice == "A" and my_choice == "X":
		return 4 # Draw 3 points + 1 point for rock
	if enemy_choice == "A" and my_choice == "Y":
		return 8 # Win 6 points + 2 points for paper
	if enemy_choice == "A" and my_choice == "Z":
		return 3 # Loss 0 points + 3 points for scissors
	if enemy_choice == "B" and my_choice == "X":
		return 1 # Loss 0 points + 1 point for rock
	if enemy_choice == "B" and my_choice == "Y":
		return 5 # Draw 3 points + 2 points for paper
	if enemy_choice == "B" and my_choice == "Z":
		return 9 # Win 6 points + 3 points for scissors
	if enemy_choice == "C" and my_choice == "X":
		return 7 # Win 6 points + 1 point for rock
	if enemy_choice == "C" and my_choice == "Y":
		return 2 # Loss 0 points + 2 points for paper
	if enemy_choice == "C" and my_choice == "Z":
		return 6 # Draw 3 points + 3 points for scissors

## With the comments in place, I only switch around returns to correspond to loss/draw/win
def evaluateRound_part2 (enemy_choice, outcome):
	if enemy_choice == "A" and my_choice == "X":
		return 3 # Loss 0 points + 3 points for scissors
	if enemy_choice == "A" and my_choice == "Y":
		return 4 # Draw 3 points + 1 point for rock
	if enemy_choice == "A" and my_choice == "Z":
		return 8 # Win 6 points + 2 points for paper
	if enemy_choice == "B" and my_choice == "X":
		return 1 # Loss 0 points + 1 point for rock
	if enemy_choice == "B" and my_choice == "Y":
		return 5 # Draw 3 points + 2 points for paper
	if enemy_choice == "B" and my_choice == "Z":
		return 9 # Win 6 points + 3 points for scissors
	if enemy_choice == "C" and my_choice == "X":
		return 2 # Loss 0 points + 2 points for paper
	if enemy_choice == "C" and my_choice == "Y":
		return 6 # Draw 3 points + 3 points for scissors
	if enemy_choice == "C" and my_choice == "Z":	
		return 7 # Win 6 points + 1 point for rock


f = open ("guide.txt")
myLines = f.readlines()
totalPoints = 0

for line in myLines:
	enemy_choice = line[0]
	my_choice = line[2]

	## Evaluate the round, add points to total
	#totalPoints += evaluateRound(enemy_choice, my_choice)
	totalPoints += evaluateRound_part2 (enemy_choice, my_choice)

print (totalPoints)
f.close()


"""
A for rock
B for paper
C for scissors

X loss
Y draw
Z win

X for rock  .......... 1
Y for paper  ......... 2
Z for scissors  ...... 3



Loss 0 points
Draw 3 points
Victory 6 points

"""