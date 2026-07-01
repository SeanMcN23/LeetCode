class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map= {}

        for num in arr:
            map[num]= map.get(num,0)+1
        lst=list(map)
        print(lst)
        lst.sort()
        print(lst)
        
        
        for x in reversed(lst):
            if x == map[x]:
                return x


        
        return -1

            

        