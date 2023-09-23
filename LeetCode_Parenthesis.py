class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for item in s:
            if item in ['(','{','[']:
                stack.append(item)
            else:
                if not stack:
                    return False
                if item == ')':
                    if stack.pop() != '(':
                        return False
                elif item == '}':
                    if stack.pop() != '{':
                        return False
                else:
                    if stack.pop() != '[':
                        return False
        if stack:
            return False
        else:
            return True


s = "[]"
sol1 = Solution()
print(sol1.isValid(s))
