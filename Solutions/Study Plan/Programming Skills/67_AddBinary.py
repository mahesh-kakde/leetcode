# case 1
a1, b1 = "11", "1"
# case 2
a2, b2 = "1010", "1011"

def sol(a, b):
    ans = []
    carry = 0

    length = max(len(a), len(b))
    a = a.zfill(length)
    b = b.zfill(length)

    for i in range(length - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        if total == 0:
            ans.insert(0, "0")
            carry = 0
            
        elif total == 1:
            ans.insert(0, "1")
            carry = 0

        elif total == 2:
            ans.insert(0, "0")
            carry = 1

        elif total == 3:
            ans.insert(0, "1")
            carry = 1

    if carry == 1:
        ans.insert(0, "1")

    return "".join(ans)

print(sol(a1, b1))
print(sol(a2, b2))