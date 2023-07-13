from typing import List


def longestConsecutive(nums: List[int]) -> int:
    hashset = set()
    for num in nums:
        hashset.add(num)
    longest_Streak = 0
    for num in nums:
        if (num-1) not in hashset:
            current_Num = num
            current_Streak = 1
            while (current_Num + 1) in hashset:
                current_Num += 1
                current_Streak += 1
            longest_Streak = max(longest_Streak, current_Streak)
    return longest_Streak


nums = [0,3,7,2,5,8,4,6,0,1]
res = longestConsecutive(nums)
print("Result : ", res)