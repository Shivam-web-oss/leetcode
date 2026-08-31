class Solution {
    public int trap(int[] height) {
    int left=0,right=height.length-1,total=0;
    int leftmax=0,rightmax=0;
    while(left<right){
        leftmax=Math.max(leftmax,height[left]);
        rightmax=Math.max(rightmax,height[right]);
        if(leftmax<rightmax){total += leftmax-height[left++];}
        else {total +=rightmax -height[right--];}
    }
    return total;
    }
}