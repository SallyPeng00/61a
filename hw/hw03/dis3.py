def is_prime(n):
	def prime_helper(k):
		if k == 1:
			return True
		elif n % k == 0 or n == 0:
			return False
		else:
			return prime_helper(k-1)

	return prime_helper(n - 1)