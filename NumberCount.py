count = [-1,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]

def hundred():
	c = 100*sum(count[1:10])
	c += 900*len("hundred")
	c += 891*len("and")
	return c+10*tens()

def tens():
	s = sum(count[1:])
	s += 8*sum(count[1:10])
	s += 10*(6+6+5+5+5+7+6+6)
	return s
	
print hundred()+len("one")+len("thousand")
