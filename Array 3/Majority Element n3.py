from typing import List


def majorityElement(nums: List[int]) -> List[int]:
    cnt1 = 0
    cnt2 = 0
    element1 = float('-inf')
    element2 = float('-inf')

    for i in range(len(nums)):
        if cnt1 == 0 and element2 != nums[i]:
            cnt1 = 1
            element1 = nums[i]
        elif cnt2 == 0 and element1 != nums[i]:
            cnt2 = 1
            element2 = nums[i]
        elif nums[i] == element1:
            cnt1 += 1
        elif nums[i] == element2:
            cnt2 += 1
        else:
            cnt2 -= 1
            cnt1 -= 1

    l = []
    cnt1 = 0
    cnt2 = 0
    for i in range(len(nums)):
        if nums[i] == element1:
            cnt1 += 1
        if nums[i] == element2:
            cnt2 += 1

    m = len(nums)//3+1
    if cnt1 >= m:
        l.append(element1)
    if cnt2 >= m:
        # if element2 not in l:
        l.append(element2)

    return l

num = [2,1,1,3,1,4,5,6]
res = majorityElement(num)
print("re", res)