class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        Sum=0
        Max=float('-inf')
        for i in range(len(nums)):
            Sum+=nums[i]
            if Sum > Max:
                Max=Sum
            if Sum<0:
                Sum=0
        return Max
solution=Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
