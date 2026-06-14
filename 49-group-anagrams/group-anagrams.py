class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #last time we did a double hashmap and basically returned that, but this time dont really have that luxury i dont believe
        map=defaultdict(list)
        # so lets think and build the logic upon this, cause its practically the same, just slighly differnet

        for word in strs:
            letters=[0]*26 # will represent a host of letters
            for letter in word:
                letters[ord(letter)-ord('a')] += 1
            map[tuple(letters)].append(word)
        return list(map.values())

            
        
        



        


        