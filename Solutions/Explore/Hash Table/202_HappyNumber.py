n1 = 19
n2 = 2
n3 = 1
n4 = 7

def sol(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        sqr = 0
        for digit in str(n):
            sqr += int(digit) ** 2
        n = sqr

    return True

print(sol(n1))
print(sol(n2))
print(sol(n3))
print(sol(n4))