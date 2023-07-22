from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        sum_ = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                sum_ += 1
                max_ = max(max_, sum_)
            else:
                sum_ = 0
        return max_