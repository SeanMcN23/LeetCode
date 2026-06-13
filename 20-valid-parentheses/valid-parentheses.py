class Solution:
    def isValid(self, s: str) -> bool:

        #super fundamental stack question:

        stack=[]
        # stack in python gotta be a list

        closedToOpen= {")":'(', ']':'[', '}':'{' }

        for bracket in s:

            if bracket in closedToOpen and stack:
                if stack[-1] == closedToOpen[bracket]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(bracket)
            
        if not stack:
            return True
        else:
            return False
                   
            
            

       


        