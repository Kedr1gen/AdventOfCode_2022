f = open("datastream.txt")

lines = f.readlines()
datastream = lines[0]
buffer = []
alternatingBuffer = []

for n in range(len(datastream)):
	not_it = True
	if len(buffer) != 14:
		buffer.append(datastream[n])

		continue
	
	# DO SHIT
	alternatingBuffer = buffer.copy()
	#print (n, alternatingBuffer)
	

	while alternatingBuffer:
		test = alternatingBuffer.pop()
		if test not in alternatingBuffer:
			continue
		else:
			not_it = False
	
	buffer.pop(0)
	
	buffer.append(datastream[n])



	if not_it:
		print("We have the marker at %d" % n)
		break
	#print(four + three + two + one)
	



f.close()