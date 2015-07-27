coins = [1,2,5,10,20,50,100,200]

ways = [0 for _ in xrange(201)]
ways[0] = 1

for i in coins:
        for j in xrange(i,201):
                ways[j] += ways[j-i]

print ways[-1]
