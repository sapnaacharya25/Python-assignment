def majority_element(nums):
    count1, count2, candidate1, candidate2 = 0, 0, None, None

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# Example usage:
nums1 = [3, 2, 3]
output1 = majority_element(nums1)
print(output1)

nums2 = [1]
output2 = majority_element(nums2)
print(output2)

nums3 = [1, 2]
output3 = majority_element(nums3)
print(output3)
