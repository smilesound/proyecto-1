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
	li=l//2
	d=("*"*li+ c +"*"*li )
	return d

def prob_5 (q,p):
	r=(q[0]*p[0] + q[1]*p[1])
	return r	


