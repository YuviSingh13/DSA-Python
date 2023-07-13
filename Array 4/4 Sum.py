from typing import List

'''
# Bruteforce approach

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    s = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        x = [nums[i], nums[j], nums[k], nums[l]]
                        x.sort()
                        if x not in s:
                            s.append(x)
    return s

'''


# Better Approach

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    trial = set()
    for i in range(n):
        for j in range(i + 1, n):
            hashset = set()
            for k in range(j + 1, n):
                l = target - (nums[i] + nums[j] + nums[k])
                if l in hashset:
                    x = [nums[i], nums[j], nums[k], l]
                    x.sort()
                    trial.add(tuple(x))
                hashset.add(nums[k])
    ans = [list(i) for i in trial]
    return ans



'''
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    ans = []

    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue

        for j in range(i+1, n):
            if j> i+1 and nums[j] == nums[j-1]: continue

            k = j+1
            l = n-1

            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1

                    while k < l  and nums[k] == nums[k-1]: k += 1

                    while k < l and nums[l] == nums[l-1]: l -= 1

                elif _sum < target: k += 1

                else: l -= 1
    return ans
'''


# nums = [1,0,-1,0,-2,2]
# target = 0

nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9

# nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
# target = 9
res = fourSum(nums, target)
print(res)