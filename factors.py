def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

n = 10
factors = find_factors(n)
print("The factors of", n, "are:", factors)