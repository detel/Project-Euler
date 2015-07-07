distinct_powers = set()

for x in xrange(2,101):
	for y in xrange(2,101):
		distinct_powers.add(x**y)

print len(distinct_powers)
