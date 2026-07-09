class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map={}
        res=[]
        for name,height in zip(names,heights):
            map[height]=name
        lst=list(map.keys())
        lst.sort(reverse=True)

        for height in lst:
            res.append(map[height])
        return res
        