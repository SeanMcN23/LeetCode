class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapT={}
        mapS={}


        for index,chara in enumerate(s): 
           
            if chara not in mapS:
                mapS[chara]=index
            if t[index] not in mapT:
                mapT[t[index]]= index
            
            if mapS[chara] != mapT[t[index]]:
                return False
        return True


