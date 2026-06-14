class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}

        for index,curr in enumerate(nums):
            num=target-curr

            if num in map:
                return [map[num],index]

            
            map[curr] = index
        return -1

            
            



               
           
       
            
        