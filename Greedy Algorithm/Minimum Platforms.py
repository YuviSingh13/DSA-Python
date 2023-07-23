class Solution:
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        plt = 1
        ans = 1
        i, j = 1, 0

        while i < n and j < n:
            if arr[i] <= dep[j]:
                plt += 1
                i += 1
            elif arr[i] > dep[j]:
                plt -= 1
                j += 1

            ans = max(ans, plt)
        return ans



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
