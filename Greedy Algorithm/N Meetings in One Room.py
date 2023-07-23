
class Solution:

    def maximumMeetings(self, n, start, end):
        l = []
        for i in range(n):
            l.append([start[i], end[i], i+1])

        l.sort(key= lambda x : x[1])

        c = 1
        k = 0
        for i in range(1, n):
            if l[i][0] > l[k][1]:
                k = i
                c += 1
        return c


# Driver Code Starts

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(n, start, end))
