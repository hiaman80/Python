# class Solution:
#     def twoSum(self, nums, target: int):
#       for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#           if nums[i] + nums[j] == target :
#             return f'[{i},{j}]'
          
# object1 = Solution()
# result = object1.twoSum([1,2,3,4,5],6)
# print(result)

# class Solution:
#     def twoSum(self, nums, target: int):
#       for i in nums:
#         if target-i in nums[nums.index(i):]:
#            return nums.index(i),nums.index(target-i)
          
# class Solution:
#     def twoSum(self, nums, target: int):
#       for i in range(len(nums)):
#         if target-nums[i] in nums[i+1:]:
#             print(i)
#             if nums[i] == target-nums[i] :
#                 nums.remove(nums[i])
#                 return i,nums.index(target-nums[i])+1
#             return i,nums.index(target-nums[i])

class Solution:
    def twoSum(self, nums, target: int):
        dict={}
        for i,n in enumerate(nums): # 0,3 : 1,2 , 2,4
            # return i,n
            if n in dict:
                return dict[n],i
            else:
                dict[target-n]=i # 3 : 0, 4:1 , 

object1 = Solution()
result = object1.twoSum([3,2,4],6)
print(result)