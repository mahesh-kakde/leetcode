n1 = 5
n2 = 7
n3 = 11

def sol(n):
    binary = list(bin(n))
    for i in range(2, len(binary)-1):
        if binary[i] == binary[i+1]:
            return False
    return True

print(sol(n1))
print(sol(n2))
print(sol(n3))