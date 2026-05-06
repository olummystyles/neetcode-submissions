class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxnum = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                # The streak continues
                count += 1
            else:
                # The number changed, so update max and reset count
                maxnum = max(maxnum, count)
                count = 0
        
        # One last check to catch the final streak
        return max(maxnum, count)