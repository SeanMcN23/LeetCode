class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #so first things first, if len of s1 is bigger, can return false since no way s2 can contain all of s1
        if len(s1) > len(s2):
            return False

        #next, what he has to do is make 2 arrays of 26 to store all of the characters and there freq in the array for comparison
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        # now we introduce the matches system, so here we go through and keep track of what matches between these 2 and what doesnt
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        # now we get into the real part
        l = 0
        
        # so now we need to start r at the index of length of s2, since permutation has to be same length, in s1

        for r in range(len(s1), len(s2)):
           # are win con
            if matches == 26:
                return True


            # now we need to make for both sides an index character, because we have to go up regardless,
            # so here these index characters will check the next index for us, if in index in s1, up matches, if not
            # subtract 1 from matches
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

            

            
            
            



