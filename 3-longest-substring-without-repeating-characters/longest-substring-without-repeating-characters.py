class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet= set()

        if len(s) == 1:
            return 1

        l,r= 0,0
        highest=0

        for r in range(len(s)):
            highest=max(highest,len(mySet))
            
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1

           # print(mySet)
            mySet.add(s[r])
        highest=max(highest,len(mySet))
        return highest

        


