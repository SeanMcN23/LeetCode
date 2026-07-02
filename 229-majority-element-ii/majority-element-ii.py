class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map={}
        res=set()

        for num in nums:
            map[num]=map.get(num,0)+1
            if map[num] > len(nums)/3:
                res.add(num)
        return list(res)
        #res=[]
        #for key in map:
            #if map[key] > len(nums)/3:
              #  res.append(key)
       # return res
