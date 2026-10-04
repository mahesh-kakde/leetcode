case1 = [[1,2,3],[4,5,6],[7,8,9]]
case2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def sol(mat):
    ans = []
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1

    while top <= bottom and left <= right:

        # left to right
        for col in range(left, right + 1):
            ans.append(mat[top][col])
        top += 1

        # top to bottom
        for row in range(top, bottom + 1):
            ans.append(mat[row][right])
        right -= 1

        # right to left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                ans.append(mat[bottom][col])
            bottom -= 1

        # bottom to top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                ans.append(mat[row][left])
            left += 1

    return ans

print(sol(case1))
print(sol(case2))