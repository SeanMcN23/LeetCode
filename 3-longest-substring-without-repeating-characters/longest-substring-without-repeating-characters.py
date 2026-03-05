class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #way better method than my first go around
        l=0
        r=0
        mySet=set()
        res=0
        #im thinking sliding window approach, so lets go with that

        for r in range(len(s)):  
            
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])

            res=max(res,len(mySet))
        return res
        
       