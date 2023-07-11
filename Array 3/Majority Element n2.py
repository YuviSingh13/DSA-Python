from typing import List


def majorityElement(nums: List[int]) -> int:
    count = 1
    element = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == element:
            count += 1
        elif count == 0:
            element = nums[i]
        else:
            count -= 1
            
    print(element)
    return element


nums = [2, 1, 1, 1, 1, 2, 2]
majorityElement(nums)