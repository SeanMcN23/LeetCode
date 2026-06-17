class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}

        for index,num in enumerate(nums):
            lookup=target-num

            if lookup in map:
                return [map[lookup],index]
            
            map[num]= index

        return []
      
            
            



               
           
       
            
        