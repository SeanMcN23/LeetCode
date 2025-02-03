class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        mySet=set()
        right=0
        highest=0
        curr=1
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        while right < len(s):
          
            if s[right] in mySet:
                left += 1
           
                mySet.clear()
                right= left
                
           
            else:
                mySet.add(s[right])

                
                right += 1
            if highest< len(mySet):
                highest=len(mySet)

                


                
           
       
        return highest
            
           


        