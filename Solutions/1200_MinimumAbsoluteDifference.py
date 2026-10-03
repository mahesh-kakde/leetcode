arr1 = [4,2,1,3]
arr2 = [1,3,6,10,15]
arr3 = [3,8,-10,23,19,-4,-14,27]
arr4 = [40,11,26,27,-20]

def sol(arr):
    arr.sort()
    diff = float('inf')
    ans = []

    for i in range(len(arr) - 1):
        diff = min(diff, abs(arr[i + 1] - arr[i]))

    for i in range(len(arr) - 1):
        if abs(arr[i + 1] - arr[i]) == diff:
            curr = []
            curr.append(arr[i])
            curr.append(arr[i + 1])
            ans.append(curr)

    return ans

print(sol(arr1))
print(sol(arr2))
print(sol(arr3))
print(sol(arr4))