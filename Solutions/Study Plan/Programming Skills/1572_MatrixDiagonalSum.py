mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
mat2 = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
mat3 = [[5]]
mat4 = [[7,9,8,6,3],
        [3,9,4,5,2],
        [8,1,10,4,10],
        [9,5,10,9,6],
        [7,2,4,10,8]]

def sol(mat):
    diag1 = []
    diag2 = []

    if len(mat) == 1:
        return mat[0][0]
    
    for i in range(len(mat)):
        diag1.append(mat[i][i])

    j = len(mat[0])
    for i in range(len(mat)):
        diag2.append(mat[i][j-1])
        j -= 1

    if len(diag2) % 2 != 0:
        diag2.pop(len(diag2)//2)

    return sum(diag1+diag2)

print(sol(mat1))
print(sol(mat2))
print(sol(mat3))
print(sol(mat4))