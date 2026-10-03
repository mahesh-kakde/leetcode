head1 = [4, 2, 1, 3]
head2 = [-1, 5, 3, 4, 0]

def sol(head):
    for i in range(1, len(head)):
        key = head[i]
        j = i - 1

        while j >= 0 and head[j] > key:
            head[j + 1] = head[j]
            j -= 1

        head[j + 1] = key

    return head

print(sol(head1))
print(sol(head2))