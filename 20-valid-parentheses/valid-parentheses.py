class Solution:
    def isValid(self, s: str) -> bool:

        #super fundamental stack question:

        stack=[]

        # we want a dicionary for our closed to open when we encounter a closed

        closedToOpen= {']':'[', ')':'(', "}":"{"}

        for bracket in s:

            if bracket in closedToOpen:
                if stack and stack[-1]==closedToOpen[bracket]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(bracket)
        if stack:
            return False
        return True
            
            

       


        