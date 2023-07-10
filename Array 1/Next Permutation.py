def nextPermutation(num):
    ind = -1
    n = len(num)
    for i in range(n-2, -1, -1):
        if num[i] < num[i+1]:
            ind = i
            break

    if ind == -1:
        num.reverse()
        return

    for i in range(n-1, ind, -1):
        if num[i] > num[ind]:
            num[i], num[ind] = num[ind], num[i]
            break

    num[ind+1:] = reversed(num[ind+1:])

    print(num)

arr = [3, 2, 1]
nextPermutation(arr)