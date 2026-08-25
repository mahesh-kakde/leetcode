case1 = [1,2,3,4,5]
case2 = [1,2,3,4,5,6]
case3 = [1,3,2,5,6,8,0]

def sol(head):
    count = 0
    curr = head

    while curr:
        count += 1
        curr = curr.next

    curr = head

    for i in range(count // 2):
        curr = curr.next

    return curr

print(sol(case1))
print(sol(case2))
print(sol(case3))