# class Solution:
#     def removeElement(self, nums, val):
#         while val in nums:
#             nums.remove(val)
#         return nums      
class Solution:
    def removeDuplicates(self, nums):
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
        return result
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))