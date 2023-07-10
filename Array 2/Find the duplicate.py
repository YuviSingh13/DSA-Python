from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

nums = [1,3,4,2,2]
res = findDuplicate(nums)
print("Duplicate number : ", res)