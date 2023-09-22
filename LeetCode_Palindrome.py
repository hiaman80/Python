class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y == y[-1::-1] :
            return True
        

obj = Solution()
result = obj.isPalindrome(121)
print(result)

# https://github.com/hiaman80/Python