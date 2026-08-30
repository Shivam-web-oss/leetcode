class Solution {
    public void duplicateZeros(int[] arr) {
        int possibleDups = 0;
        int length_ = arr.length - 1;

        // Count zeros to determine shift boundary
        for (int left = 0; left <= length_ - possibleDups; left++) {
            if (arr[left] == 0) {
                // Edge case: zero cannot be duplicated because it's at the boundary
                if (left == length_ - possibleDups) {
                    arr[length_] = 0;
                    length_--;
                    break;
                }
                possibleDups++;
            }
        }

        // Copy elements backwards
        int last = length_ - possibleDups;
        for (int i = last; i >= 0; i--) {
            if (arr[i] == 0) {
                arr[i + possibleDups] = 0;
                possibleDups--;
                arr[i + possibleDups] = 0;
            } else {
                arr[i + possibleDups] = arr[i];
            }
        }
    }
}