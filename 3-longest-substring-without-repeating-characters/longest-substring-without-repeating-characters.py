class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        mySet=set()
        highest=0
        l,r=0,0

        for r in range(len(s)):
           
            while s[r] in mySet:
                mySet.remove(s[l])
                l+= 1

    
            mySet.add(s[r])
            highest=max(highest,len(mySet))
        return highest


            
      


        


