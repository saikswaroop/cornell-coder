""" Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """

fib = []
fib.append(1)
fib.append(2)
fib.append(3)

fibSum = []
fibSum.append(2)

fibNum = 3
i = 3

while(fibNum < 4000000):
	
	if(fibNum % 2 == 0):
		fibSum.append(fibNum)
		
	fibNum = fib[i-1] + fib[i-2]
	print fibNum
	fib.append(fibNum)
	i = i + 1

sum = 0
for r in range(len(fibSum)):
	sum = sum + fibSum[r]
	
print "SUM:", sum