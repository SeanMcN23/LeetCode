class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}

        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            map[num]= map.get(num,0) +1
        for num, cnt in map.items():
            freq[cnt].append(num)
        result=[]

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) ==k:
                    return result
        

        
            
            

        