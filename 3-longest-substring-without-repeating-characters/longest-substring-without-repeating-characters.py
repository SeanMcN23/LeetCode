class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        mySet=set()

        highest=0

        for c in s:
            while c in mySet:
                mySet.remove(s[l])
                l += 1

            mySet.add(c)
            highest=max(highest,len(mySet))
        return highest
        
        


