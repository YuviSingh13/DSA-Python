def maxSubArray(num):
    s = 0
    mx = -99999
    for i in range(len(num)):
        s += num[i]
        if s < 0:
            s = 0
        if s > mx:
            mx = s
    print(mx)



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray(nums)