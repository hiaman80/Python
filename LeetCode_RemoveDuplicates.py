class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return nums      

nums = [0,1,2,2,3,0,4,2]
sol = Solution()
print(sol.removeElement(nums,2))