class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        n1, n2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(n1)] for _ in range(n2)]
        for i2 in range(n2):
            for i1 in range(n1):
                if nums1[i1] == nums2[i2]:
                    if i1 == 0 or i2 == 0:
                        dp[i2][i1] = 1
                    else:
                        dp[i2][i1] = 1 + dp[i2-1][i1-1]
                result = max(result, dp[i2][i1])
        return result
