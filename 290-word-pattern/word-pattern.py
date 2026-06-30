class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # just map each letter to a word in s im thinking
        map={}
        words=s.split()
        word_track={}

        if len(pattern) != len(words):
            return False
    


        for index, letter in enumerate(pattern):
            print(map)
            print(word_track)
            if letter in map:
                if map[letter] != words[index]:
                    return False
            if words[index] in word_track:
                if word_track[words[index]] != letter:
                    return False
               

            map[letter] = words[index]
            word_track[words[index]] = letter

        return True


        
        