height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1,1]

def sol(height):
    l = 0
    r = len(height) - 1
    ans = 0

    while l < r:
        width = r - l
        heightt = min(height[l], height[r])
        area  = width * heightt
        ans = max(ans, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans

print(sol(height1)) # 49
print(sol(height2)) # 1