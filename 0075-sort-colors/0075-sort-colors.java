class Solution {
    public void sortColors(int[] nums) {
         int i=0,j=0,k=nums.length-1;
    while(i<=k){
        if(nums[i]==0){
            swap(nums,i,j);
            j++;
            i++;
        }else if(nums[i]==1){
            i++;
        }else{
            swap(nums,i,k);
            k--;
        }
    }

    }
    private void swap(int[] nums,int a,int b){
            int temp=nums[a];
            nums[a]=nums[b];
            nums[b]=temp;
         }
}