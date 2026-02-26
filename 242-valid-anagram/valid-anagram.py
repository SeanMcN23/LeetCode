class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # lets do this one tomorrow, will do this, binary search, sliding window, then we do some med diff on hashings and arrays
        hashmap1={}
        hashmap2={}

        for x in s:
            if x in hashmap1:
                hashmap1[x] += 1
            else:
                hashmap1[x] = 1
        for x in t:
            if x in hashmap2:
                hashmap2[x] += 1
            else:
                hashmap2[x] = 1
        return hashmap1 == hashmap2

        


            
        

        
