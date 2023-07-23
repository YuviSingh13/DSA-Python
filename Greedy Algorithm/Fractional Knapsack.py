class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    def fractionalknapsack(self, W, arr, n):
        arr.sort(key= lambda x : x.value / x.weight, reverse=True)
        curweight = 0
        finalvalue = 0.0
        for i in range(n):
            if curweight + arr[i].weight <= W:
                curweight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W - curweight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue







class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, arr, n))