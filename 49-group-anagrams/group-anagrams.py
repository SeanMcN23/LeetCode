class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #last time we did a double hashmap and basically returned that, but this time dont really have that luxury i dont believe
        map=defaultdict(list)
        # so lets think and build the logic upon this, cause its practically the same, just slighly differnet
        for s in strs:
            count= [0]*26 # for each letter in alphabet
            for c in s:
                count[ord(c)-ord("a")] += 1
            map[tuple(count)].append(s)
        return list(map.values())
         



        


        