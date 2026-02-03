class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset1={}
        hashset2={}
        if len(s) != len(t):
            return False

        for x in s:
            if x in hashset1:
                hashset1[x] += 1
            else:
                hashset1[x]=1
        for x in t:
            if x in hashset2:
                hashset2[x] += 1
            else:
                hashset2[x]=1
        # im thinking that now what i should do is see if all of s elements are in hashset2 and all of t elements are in hashset1
        return hashset1 == hashset2
            
        

        
