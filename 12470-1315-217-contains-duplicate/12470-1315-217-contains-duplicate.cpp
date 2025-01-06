class Solution {
public:
// n^2 solution, itll work but better way of doing it
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> myHash;

        for(int i=0;i<nums.size();i++){
            auto it=myHash.find(nums[i]);
            if(it != myHash.end()){
                return true;
            }
            myHash.insert(nums[i]);
        }
        return false;
            

        
    }
};