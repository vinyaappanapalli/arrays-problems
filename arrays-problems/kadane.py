# Problem: Maximum Subarray (Kadane’s Algorithm)

# Approach:
# Keep track of current sum and maximum sum

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

# Example
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

# Time Complexity: O(n)
# Space Complexity: O(1)