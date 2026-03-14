class Solution {
    public List<Integer> findDuplicates(int[] nums) {

        Set<Integer> mySet= new HashSet<>();
        ArrayList<Integer> arr = new ArrayList<>();

        for(int num: nums){
            if(mySet.contains(num)){
                arr.add(num);

            }
            else{
                mySet.add(num);

            }


        }
        return arr;


        
    }
}