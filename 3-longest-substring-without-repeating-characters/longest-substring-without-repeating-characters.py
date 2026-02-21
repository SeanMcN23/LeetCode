class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #way better method than my first go around
        left=0
        right=0
        mySet=set()
        res=0

        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            mySet.add(s[right])
            res=max(res,len(mySet))
        return res



           


        