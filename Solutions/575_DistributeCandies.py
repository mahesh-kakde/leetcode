candy1 = [1,1,2,2,3,3]
candy2 = [1,1,2,3]
candy3 = [6,6,6,6]

def sol(candy):
    n = len(candy) // 2
    candy = set(candy)

    if n <= len(candy):
        return n
    return len(candy)

print(sol(candy1))
print(sol(candy2))
print(sol(candy3))