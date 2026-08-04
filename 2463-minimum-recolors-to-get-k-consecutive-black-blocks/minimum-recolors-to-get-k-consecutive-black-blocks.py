class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # so im thinking, i might want a hashamp for this to help me keep track, i think of the black vs white
        # really just trying to grab a window size of k right? so with that in mind, thinking of having a min variable as well to help me keep track

        res= float('inf')
        l=0
        myMap={}

        for r in range(len(blocks)):
            myMap[blocks[r]] = myMap.get(blocks[r],0) + 1

            if(r-l) + 1 > k:
                myMap[blocks[l]] -= 1
                l += 1
            
            if(r-l) +1 == k:   
                res = min(res,myMap.get('W',0))
               

            
        return res


        