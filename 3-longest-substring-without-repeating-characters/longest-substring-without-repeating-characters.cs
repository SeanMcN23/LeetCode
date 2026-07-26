

public class Solution {
    public int LengthOfLongestSubstring(string s) {

        int l=0;
        HashSet<int> myHash= new HashSet<int>();
        int longest=0;
        
        for(int r=0;r<s.Length;r++){

            while(myHash.Contains(s[r])){
               
                myHash.Remove(s[l]);
                l ++;

            }
            myHash.Add(s[r]);
            longest=Math.Max(longest,myHash.Count);


        }
        return longest;
        
    }
}