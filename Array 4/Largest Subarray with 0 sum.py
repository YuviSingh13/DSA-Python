def maxLen(n, arr):
    d = {}
    max_i = 0
    _sum = 0
    for i in range(n):
        _sum += arr[i]
        if _sum == 0:
            max_i = i + 1
        else:
            if _sum in d:
                max_i = max(max_i, i-d[_sum])
            else:
                d[_sum] = i
    return max_i



num = [-1, 1, -1, 1]
res = maxLen(len(num), num)
print("res : ", res)