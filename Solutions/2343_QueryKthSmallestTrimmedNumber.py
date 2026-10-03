nums1, queries1 = ["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]
nums2, queries2 = ["24","37","96","04"], [[2,1],[2,2]]

def sol(nums, queries):
    ans = []

    for k, trim in queries:
        trimmed = []

        for i, num in enumerate(nums):
            trimmed.append((num[-trim:], i))

        trimmed.sort()
        ans.append(trimmed[k - 1][1])

    return ans

print(sol(nums1, queries1))
print(sol(nums2, queries2))