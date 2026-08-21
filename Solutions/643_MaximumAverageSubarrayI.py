case1 = [1,12,-5,-6,50,3]
case2 = [5]

# NOT ACCEPTED
def maxAverage(nums, k):
    max_average = float("-inf")

    for i in range(len(nums) - k + 1):
        total = 0
        for j in range(i, i + k):
            total += nums[j]

        average = total / k
        max_average = max(max_average, average)

    return max_average

print(maxAverage(case1, 4))
print(maxAverage(case2, 1))

# ACCEPTED
def maxAverage(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k]

        max_sum = max(max_sum, current_sum)

    return max_sum / k

print(maxAverage(case1, 4))
print(maxAverage(case2, 1))


# OPTIMAL (SLIDING WINDOW)
def maxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    left = 0

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[left]

        left += 1

        max_sum = max(max_sum, window_sum)

    return max_sum / k

print(maxAverage(case1, 4))
print(maxAverage(case2, 1))