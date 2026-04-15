# Problem: Maximum Sum Subarray of Size K

# Approach:
# Use sliding window to maintain sum of size k

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]      # add next element
        window_sum -= nums[i - k]  # remove first element of window
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))

# Time Complexity: O(n)
# Space Complexity: O(1)