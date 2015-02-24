public class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        if (n <= 1) return;
        k = k % n;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }
    public void reverse(int[] nums, int left, int right){
        int n = right - left + 1;
        for(int i = left; i < left + n / 2; i++){
        	int offset = i - left;
            int temp = nums[i];
            nums[i] = nums[right - offset];
            nums[right - offset] = temp;
        }
    }
    
}
