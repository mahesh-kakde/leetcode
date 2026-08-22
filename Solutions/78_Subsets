case1 = [1, 2, 3]
case2 = [0]

# ACCEPTED (RECURSIVE BACKTRACKING)
def subsets(nums):
    result = [[]]

    for num in nums:
        new_subsets = []
        for subset in result:
            new_subset = subset + [num]
            new_subsets.append(new_subset)

        result.extend(new_subsets)

    return result

print(subsets(case1))
print(subsets(case2))