class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
         int t=m+n,c=0;
    
    for(int i=m;i<t;i++){
        nums1[i]=nums2[c];
        c++;
    }
    Arrays.sort(nums1);
    System.out.print(nums1);
    }
}