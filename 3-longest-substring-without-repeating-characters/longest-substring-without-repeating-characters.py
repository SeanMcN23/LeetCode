class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        mySet=set()


        res,scout= 0,0
        highest=0

        for scout in range(len(s)):
            
            while s[scout] in mySet:
                mySet.remove(s[res])
                res+= 1

            mySet.add(s[scout])
            highest=max(highest,len(mySet))
        return highest