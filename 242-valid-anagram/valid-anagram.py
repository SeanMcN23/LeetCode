class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # lets do this one tomorrow, will do this, binary search, sliding window, then we do some med diff on hashings and arrays
        map1={}
        map2={}

        for x in s:
            map1[x]= map1.get(x,0) + 1
        for y in t:
             map2[y]= map2.get(y,0) + 1
        
        return map1 == map2
        
        



        

        


            
        

        
