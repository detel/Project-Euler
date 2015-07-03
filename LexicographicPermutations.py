from itertools import permutations

list = sorted([ ''.join(p) for p in permutations('0123456789')])
print list[999999]
