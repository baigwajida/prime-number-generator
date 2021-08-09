def prime_sieve(n):
	prime = [] 							# an empty list
	for i in range (n + 1):
		prime.append(i)					# append all the number one by one starting from 2
	prime[0] = 0
	prime[1] = 0
	p = 2
	while(p * p <= n):
		if (p != 0):					# if prime[p] is not changed, then it is a prime
			for i in range (p*2, n+1, p):	
				prime[i] = 0			# update all multiples of p to zero
		p +=1
	print("All prime numbers upto ", n, " are : " )	# print all elements of the list which are non-zero
	for i in range(len(prime)):
		if (prime[i] != 0):
			print(prime[i], end=" ")

n = int(input("Enter an integer number : "))
prime_sieve(n)
