class Solution {
    public int sumOfUnique(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num: nums) {
            map.put(num ,map.getOrDefault(num,0)+ 1);
        }
        int sum = 0;
        for (Map.Entry<Integer,Integer> entry :map.entrySet()) {
            int num = entry.getKey();
            int count=entry.getValue();
            if (count == 1) {
                sum += num;
            }
        }

        return sum;
    }
}