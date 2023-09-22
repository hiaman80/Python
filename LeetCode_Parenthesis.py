# class Solution:
#     def isValid(self, s):
#         stack = []
#         if len(s) % 2 != 0:
#             return False
#         for item in s:
#             if item in ['(','{','['] :
#                 stack.append(item)
#             else:
#                 if not stack:
#                     return False
            


#             pass






class Solution:
    def isValid(self, s):
        stack = []

        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            else:
                if not stack:
                    return False
                else :
                    if item == ')':
                        if stack.pop()!='(':
                            return False
                    
                    elif item == '}':
                        if stack.pop()!='{':
                            return False
                    else:
                        if item == ']':
                            if stack.pop()!='[':
                                return False     
        if stack:          
            return False
        return True


s = "[]"
sol1 = Solution()
print(sol1.isValid(s))
