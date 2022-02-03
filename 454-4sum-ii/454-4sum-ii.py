class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum1 , sum2 = [], defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum1.append(nums1[i] + nums2[j])
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sum2[nums3[i] + nums4[j]] += 1
        result = 0
        for num in sum1:
            result += sum2[-1 * num]
        return result
                