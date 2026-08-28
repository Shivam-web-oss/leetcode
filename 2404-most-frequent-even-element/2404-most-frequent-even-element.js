/**
 * @param {number[]} nums
 * @return {number}
 */
var mostFrequentEven = function(nums) {
        // Implement your solution here
        let map =new Map;
        for (let num of nums){
            if (num%2===0){
                map.set(num,(map.get(num)||0)+1);
            }
        }
        let ans=-1,max=0;
        for (let [num,c] of map){
            if (c>max){
                max=c;
                ans=num;
            }else if (c == max) {
                ans = Math.min(ans, num);
            }
        }
        return ans;
};