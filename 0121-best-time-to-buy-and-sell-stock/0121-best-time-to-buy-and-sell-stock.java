class Solution {
    public int maxProfit(int[] prices) {
        int maxpro=0,min=prices[0];
    for (int i=0;i<prices.length;i++){
        if(prices[i]<min){
            min=prices[i];      
        }
        maxpro=Math.max(maxpro,prices[i]-min);
    }
    return maxpro;
    }
}