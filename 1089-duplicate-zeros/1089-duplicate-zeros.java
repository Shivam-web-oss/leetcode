class Solution {
    public void duplicateZeros(int[] arr) {
        int n = arr.length;
        int[] res= Arrays.copyOf(arr, n);
        int i=0;
        int j=0;
        while(i<n && j<n){
            arr[j] = res[i];
            j++;
            if (res[i] == 0 && j < n) {
                arr[j] = 0;
                j++;
            }
            i++;
        }
        return;
    }
}