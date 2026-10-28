matrix1, target1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
matrix2, target2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13

def sol(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    t = m * n
    l = 0
    r = t - 1

    while l <= r:
        m = (l + r) // 2
        i = m // n
        j  = m % n
        mid = matrix[i][j]

        if target == mid:
            return True
        elif target < mid:
            r = m - 1
        else:
            l  = m + 1

    return False

print(sol(matrix1, target1))
print(sol(matrix2, target2))