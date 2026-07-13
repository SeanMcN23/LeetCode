class Solution:
    def compress(self, chars: List[str]) -> int:
        l,r=0,0
        mySet=set()
       

        while r != len(chars):
            mySet.add(chars[r])
            counter =0
            while r != len(chars) and chars[r] in mySet:
                counter += 1
                r += 1
            mySet.remove(chars[r-1])
            counter = str(counter)
            chars[l] = chars[r-1]
            
            l += 1

            print(counter)
            if counter != '1':
                for num in counter:
                    chars[l] = num
                    l += 1


            
            
        return l


            

            
        