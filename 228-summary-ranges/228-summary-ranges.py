class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        stack = [nums[0]] if len(nums) > 0 else nums
        for num in nums[1:]:
            if stack :
                if stack[-1] == num - 1:
                    stack.append(num)
                else:
                    if len(stack) > 1:
                        result.append(f'{stack[0]}->{stack[-1]}')
                    else:
                        result.append(f'{stack[0]}')
                    stack = [num]
            else:
                stack.append(num)
        if len(stack) == 1: result.append(f'{stack[0]}')
        elif len(stack) > 1: result.append(f'{stack[0]}->{stack[-1]}')
            
        return result