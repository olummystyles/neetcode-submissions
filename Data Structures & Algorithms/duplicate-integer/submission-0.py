class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        if not nums or len(nums)<1:
            return False
        """
        duplicate= []
        count = 1  # Start at 1 because the first number is a streak of 1
        """

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            
        return False
        
        