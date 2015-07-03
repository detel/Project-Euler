triangle = []
i = -1
#fo = open("/home/deepit/Desktop/p067_triangle.txt", "r")
with open('/home/deepit/Desktop/p067_triangle.txt') as fp:
    for line in fp:
		triangle.append(map(int,line.split()))
		i += 1
		if i != 0:
			for j in xrange(len(triangle[i])):
				if j == 0:
					triangle[i][j] += triangle[i-1][j]
				elif j == len(triangle[i])-1:
					triangle[i][j] += triangle[i-1][j-1]
				else:
					triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])

#print triangle
print max(triangle[-1])
