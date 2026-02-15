class Solution:
    def isValid(self, s: str) -> bool:
         # the idea is to use stack, since we care about order and make sure everything is there
         # use a stack and also use a hashmap defing each aspect

         # its close to open since we always need to start with an open anyway but if a close exists then we just pop 
         # the first element since that should be the opening bracket

        stack=[]
        closeToOpen={")": "(" , "]":"[" , "}":"{" }
            # so now we need to make sure stack exists as well as make sure]
            # need to check if in stack
        for x in s:
            if x in closeToOpen:
                if stack and stack[-1] == closeToOpen[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False
        

