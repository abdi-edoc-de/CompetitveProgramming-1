class Solution:
	def winnerSquareGame(self, n: int) -> bool:

		dp = [None] * (n + 1)
		dp[0] = False
		steps = sorted([ele ** 2 for ele in range(1, int(math.sqrt(n)) + 1)], reverse=True)

		for i in range(n):
			for step in steps:
				if i + step <= n:
					if dp[i + step]:
						continue
					else:
						dp[i + step] = (False if dp[i] else True)
			if dp[-1]:
				return True
		return False