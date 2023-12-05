from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    dq = deque()

    for i in range(len(nums)):
        # Remove elements outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements as they will not be the maximum in the current window
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Append the maximum to the result when the window is formed
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example usage:
nums1 = [1]
k1 = 1
output1 = maxSlidingWindow(nums1, k1)
print(output1)

nums2 = [1, 3, -1, -3, 5, 3, 6, 7]
k2 = 3
output2 = maxSlidingWindow(nums2, k2)
print(output2)
