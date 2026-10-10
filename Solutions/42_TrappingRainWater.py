height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]

def sol(height):
    left_wall = 0
    right_wall = 0
    left_max = [0] * len(height)
    right_max = [0] * len(height)
    ans = 0

    for i in range(len(height)):
        j = -i - 1
        left_max[i] = left_wall
        right_max[j] = right_wall
        left_wall = max(left_wall, height[i])
        right_wall = max(right_wall, height[j])

    for i in range(len(height)):
        pot = min(left_max[i], right_max[i])
        ans += max(0, pot - height[i])

    return ans

print(sol(height1)) # 6
print(sol(height2)) # 9