import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        HashMap<Integer, String> map = new HashMap<>();

        for (int i = 0; i < names.length; i++) {
            map.put(heights[i], names[i]);
        }

        // Sort in ascending order
        Arrays.sort(heights);

        // Fill result array in reverse (descending order)
        String[] result = new String[names.length];
        int n = heights.length;
        for (int i = 0; i < n; i++) {
            result[i] = map.get(heights[n - 1 - i]);
        }

        return result;
    }
}