class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arrayS1, arrayS2 = [0]*26, [0]*26

        # build counts correctly
        for i in range(len(s1)):
            arrayS1[ord(s1[i]) - ord('a')] += 1
            arrayS2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if arrayS1[i] == arrayS2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # add right char
            index = ord(s2[r]) - ord('a')
            arrayS2[index] += 1
            if arrayS1[index] == arrayS2[index]:
                matches += 1
            elif arrayS1[index] + 1 == arrayS2[index]:
                matches -= 1

            # remove left char
            index = ord(s2[l]) - ord('a')
            arrayS2[index] -= 1
            if arrayS1[index] == arrayS2[index]:
                matches += 1
            elif arrayS1[index] - 1 == arrayS2[index]:
                matches -= 1

            l += 1

        return matches == 26