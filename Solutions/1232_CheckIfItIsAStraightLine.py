coordinates1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

def sol(coordinates):
    ans = []

    for i in range(len(coordinates) - 1):
        x1 = coordinates[i][0]
        x2 = coordinates[i + 1][0]
        y1 = coordinates[i][1]
        y2 = coordinates[i + 1][1]

        if x2 == x1:
            ans.append(float('inf'))
        else:
            m = (y2 - y1) / (x2 - x1)
            ans.append(m)

    for i in range(len(ans) - 1):
        if ans[i] != ans[i + 1]:
            return False

    return True

print(sol(coordinates1))
print(sol(coordinates2))