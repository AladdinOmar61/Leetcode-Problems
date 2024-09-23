class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i+1 < len(nums):
            if nums[i+1] == nums[i]:
                nums.remove(nums[i+1])
            else:
                i+=1
        k = len(nums)
        return k
        # [1,1,2]