class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so we start with a map, this will count for us what we have

        count = {}

        # now we need this freq here, this will be the reverse bucket list idea, where we store the numbers for how freq they appear
        # and its bounded by however long the list we are getting is
        freq = [[] for i in range(len(nums) + 1)]
        # count and sort like normal the map
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # now we need to do the freq side, so we must make sure the value is a list remember
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        #store results in seperate list

        # now we need to go through the freq, so I in range of the length of the freq, 0 is the end and -1 means go backwards
        # once len of res is k, we can just go ahead and return it
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
            
            

        