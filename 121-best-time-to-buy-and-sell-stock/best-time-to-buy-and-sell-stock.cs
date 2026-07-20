public class Solution {
    public int MaxProfit(int[] prices) {

        int highest=0;
        int l=0;
        for(int i=0;i<prices.Length;i++){
            while(prices[l] > prices[i]){
                l ++;
            }
            if(prices[i] > prices[l]){
                highest=Math.Max(highest,prices[i]-prices[l]);
            }
        }
        return highest;


        
    }
}
