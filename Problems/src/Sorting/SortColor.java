public class SortColor {
    public void sortColors(int[] nums) {
        int left = 0;
        int zeroIdx = -1;
        int twoIdx = nums.length;
        
        while (left < twoIdx) {
            switch (nums[left]) {
                case 0: swap(nums, ++zeroIdx, left);
                        if (left == zeroIdx) {
                            ++left;
                        }
                        break;
                case 1: ++left;
                        break;
                case 2: swap(nums, --twoIdx, left);
                        break;
            }
        }
    }
    void swap(int[] nums, int idx1, int idx2) {
        if (idx1 != idx2) {
            int tmp = nums[idx1];
            nums[idx1] = nums[idx2];
            nums[idx2] = tmp;
        }
    }
}
