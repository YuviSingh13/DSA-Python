class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key= lambda x: x.profit, reverse=True)
        max_ = Jobs[0].deadline
        for i in range(1, n):
            max_ = max(max_, Jobs[i].deadline)

        slot = [-1] * (max_+1)
        countJobs = 0
        jobProfit = 0

        for i in range(n):
            for j in range(Jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += Jobs[i].profit
                    break

        return countJobs, jobProfit


class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        print("Here : ", Jobs)
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])