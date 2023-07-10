from typing import List


def swapIfGreater(num1, num2, ind1, ind2):
    if num1[ind1] > num2[ind2]:
        num1[ind1], num2[ind2] = num2[ind2], num1[ind1]


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    l = m+n
    gap = (l // 2) + (l % 2)

    while gap > 0:
        print(nums1, nums2, gap)
        left = 0
        right = left+gap
        while right < l:
            print(m, left, right)
            if left < m and right >= m:
                swapIfGreater(nums1, nums2, left, right-m)
            elif left >= m:
                swapIfGreater(nums2, nums2, left-m, right-m)
            else:
                swapIfGreater(nums1, nums2, left, right)
            left += 1
            right += 1

        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)

    for i in range(n):
        nums1[m+i] = nums2[i]
    print("Final : ", nums1)


# m = 3
# nums1 = [1,2,3,0,0,0]
# n = 3
# nums2 = [2,5,6]


# m = 0
# nums1 = [0]
# n = 1
# nums2 = [1]


# nums1 = [4,0,0,0,0,0]
# m = 1
# nums2 = [1,2,3,5,6]
# n = 5

nums1 = [1, 2, 3, 4, 5]
m = 5
nums2 = []
n = 0


merge(nums1, m, nums2, n)