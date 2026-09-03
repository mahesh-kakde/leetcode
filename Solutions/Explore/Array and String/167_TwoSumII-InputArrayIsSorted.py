# case 1
numbers1, target1 = [2,7,11,15], 9
# case 2
numbers2, target2  = [2,3,4], 6
# case 3
numbers3, target3  = [-1,0], -1

def sol(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

print(sol(numbers1, target1))
print(sol(numbers2, target2))
print(sol(numbers3, target3))