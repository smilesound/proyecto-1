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

def prob_5 (a,b):
	r=(a[0]*b[0])+(a[1]*b[1])
	return r

def prob_6 (q):
	q.sort()
	q.reverse()
	return q

def prob_7():
	m=[]
	for i in range(1000):
		if i%4==0 or i%7==0:
			m.append(i)
	return m
	
def prob_8(p):
	p=p+1
	h= p+1
	for i in range (p):
		num = i
		h=h-1
		tri= (" "*(h-1)+ " *" * num )			
		return tri



