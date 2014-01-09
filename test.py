def choose(n,k):
    if k == 0:
    	return 1.0
    return float((n * choose(n - 1, k - 1)) / k)

print choose(4,7)