n1 = 6
n2 = 1
n3 = 14

def sol(n):
    factors = [2, 3, 5]

    if n == 0:
        return False
    
    for factor in factors:
        while n % factor == 0:
            n = n//factor

    return n == 1

print(sol(n1))
print(sol(n2))
print(sol(n3))