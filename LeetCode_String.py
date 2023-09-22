# # My Solution
# class Solution:
#     def longestCommonPrefix(self, strs):
#         small = strs[0]
#         for i in range(len(strs)):
#             if len(strs[i]) < len(small) :
#                 small = strs[i]
#         # small = flow
#         for ele in strs:
#             for j in range(len(small)):
#                 if small not in ele[:len(small)] :
#                     small = small[:-1]
#                     if small == '' :
#                         return ''
#                 else:
#                     break
#         return small
            
# sol = Solution()
# strs = ["flower","flow","flight"]
# result = sol.longestCommonPrefix(strs)
# print(result)


class Solution:
    def longestCommonPrefix(self, v):
        ans=""
        v=sorted(v)
        print(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
sol = Solution()
strs = ["flower","flow","flight"]
result = sol.longestCommonPrefix(strs)
print(result)