def paths(num):
	distance = [[0 for i in xrange(num+1)] for j in xrange(num+1)]

	distance[0][0] = 0
	for i in xrange(1,num+1):
		distance[i][0] = 1
	for j in xrange(1,num+1):
		distance[0][j] = 1

	for i in xrange(1,num+1):
		for j in xrange(1,num+1):
			distance[i][j] = distance[i-1][j] + distance[i][j-1]

	return distance[num][num]

print paths(20)
