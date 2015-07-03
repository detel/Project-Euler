from sys import stdin

triangle = []

for i in xrange(15):
	triangle.append(map(int,stdin.readline().split()))
	if i != 0:
		for j in xrange(len(triangle[i])):
			if j == 0:
				triangle[i][j] += triangle[i-1][j]
			elif j == len(triangle[i])-1:
				triangle[i][j] += triangle[i-1][j-1]
			else:
				triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])

print max(triangle[-1])
