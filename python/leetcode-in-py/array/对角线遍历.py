#coding=gbk


A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = []

m = len(A)
n = len(A[0])
a, b = 0, 0

for i  in range(m):
	for j in range(n):
		tem = A[a][b]
		B.append(tem)
		print(B)
		# 偶数列，向右上角移动（-1， 1）
		if (a+b) % 2 == 0:
			a -= 1
			b += 1

			if a<0 and b > n:
				a -=2
				b = n-1
			if a<0:
				a = 0
				
		else:
			a += 1
			b -= 1
			if a > m and b<0:
			    a = m - 1
			    b = n + 2
			if b < 0:
				b = 0


print(B)
