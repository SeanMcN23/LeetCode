class Solution:
    def isHappy(self, n: int) -> bool:
        mySet=set()

        while n != 1:
            if n in mySet:
                return False
            mySet.add(n)
            l,r=0,len(list(str(n))) -1
            temp=0
            while l<=r :
                temp += int(list(str(n))[l]) **2
                
                if l != r:
                    temp += int(list(str(n))[r]) **2
                l += 1
                r -= 1
            n=temp

        return True
                
