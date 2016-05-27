def prob_1 (n):
	return n%2==0

def prob_2 (n):
	b=n-32/1.8
	return b 

def prob_3(b,p):
	p=b
	for i in range (1,p):
		b=b*p
	return b

def prob_4(c,l):
	h=len(c)
	li=l-h
	li=li//2
	ld=l-li
	return ("*"*li, c , )
