class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #last time we did a double hashmap and basically returned that, but this time dont really have that luxury i dont believe

        mylist= defaultdict(list)

        for word in strs:
            letters=[0]*26
            for c in word:
                letters[ord(c)-ord('a')] += 1
            mylist[tuple(letters)].append(word)
        return list(mylist.values())

        
            
        
        



        


        