class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map={}

        for num in nums:
            map[num]=map.get(num,0)+1

        res=[]
        for key in map:
            if map[key] > len(nums)/3:
                res.append(key)
        return res
