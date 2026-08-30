case1 = [[1,2,3],[4,5,6],[7,8,9]]
case2 = [[1,2],[3,4]]

def sol(mat):
    ans = []
    rows = len(mat)
    cols = len(mat[0])
    row = 0
    col = 0
    direction = 1  # 1 = up right, -1 = down left

    for _ in range(rows * cols):
        ans.append(mat[row][col])

        if direction == 1:  # up right
            if col == cols - 1:
                row += 1
                direction = -1
            elif row == 0:
                col += 1
                direction = -1
            else:
                row -= 1
                col += 1

        else:  # down left
            if row == rows - 1:
                col += 1
                direction = 1
            elif col == 0:
                row += 1
                direction = 1
            else:
                row += 1
                col -= 1

    return ans

print(sol(case1))
print(sol(case2))