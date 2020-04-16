# def valores():
# 	global a,b,c
# 	a = 1
# 	b = 2
# 	c = 3
# 	print(a,b,c)
	
# #Escopo Global e Escopo Local 
# a = 5
# b = 4
# c = 7
# print (a,b,c)
# valores()
# print(a, b, c)

def soma(*n):
	s = 0 
	for i in n:
		s += int(i)
	return s
	
r1 = soma(5,5)
print (r1)