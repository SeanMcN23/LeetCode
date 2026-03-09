class Solution:
    def isValid(self, s: str) -> bool:
         #i need a stack but i also need a map of what im looking for
         
         stack=[]
         closeToOpen={")":"(","]":"[","}":"{"}

         for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
         return True if not stack else False

        

