def solution(n, m):
	def get_gcd(a, b):
		while b > 0:
			a, b = b, a % b
		return a
	
	gcd_value = get_gcd(n, m)
	lcm_value = (n*m) // gcd_value
	
	return [gcd_value, lcm_value]