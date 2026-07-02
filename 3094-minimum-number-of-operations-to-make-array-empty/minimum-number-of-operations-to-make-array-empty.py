class Solution:
    def minOperations(self, nums: List[int]) -> int:

        map={}
        for num in nums:
            map[num]=map.get(num,0)+1
        print(map)
        result=0
        for key in map:
            if map[key] ==1:
                return -1
            else:
                result += math.ceil(map[key]/3)
        return result


        