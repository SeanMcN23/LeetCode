class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash1={}
        for x in nums:
            if x in myHash1:
                myHash1[x] += 1
            else:
                myHash1[x] = 1
        
        queue=[]
        for num, amount in myHash1.items():
            queue.append([amount,num])
        queue.sort()

        res=[]
        while len(res) < k:
            res.append(queue.pop()[1])
        return res
            
            

        