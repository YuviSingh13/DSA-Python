class Solution:
	def minCoins(self, coins, M, V):
		'''
		# Greedy Approach
		# deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
		coins.sort()
		print(coins, "M = ", M)
		l = []
		for j in range(M-1, -1, -1):
			while V >= coins[j]:
				V -= coins[j]
				l.append(coins[j])
		print(l, "deno")
		if len(l) == 0:
			return -1
		return len(l)
		'''

		# DP Approach
		dp = [V+1] * (V+1)
		dp[0] = 0

		for a in range(1, V+1):
			for c in coins:
				if a-c >= 0:
					dp[a] = min(dp[a], 1+dp[a-c])

		return dp[V] if dp[V] != V+1 else -1



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)