
/**
 * Solution 1: sort the array and return the kth element. O(nlogn)
 * Solution 2: build min-heap with n elements and return the kth element popped from the heap. O(n + klogn)
 * Solution 3: build max-heap with k elements
 * Solution 4: quicksort
 **/

class Solution3 {

  public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue();

        for (int num : nums) {
            if (queue.size() < k)
                queue.add(num);
            else {
                int kth = queue.peek();
                if (kth < num) {
                    queue.poll();
                    queue.add(num);
                }
            }
        }
        return queue.peek();
    }
}


class Solution4 {

  public int findKthLargest(int[] nums, int k) {
        if (nums == null || nums.length == 0) return 0;

        randomize(nums);
        k--;
        int n = nums.length;
        int p = partition(nums, 0, n - 1);
        while (p != k) {
            if (p < k) p = partition(nums, p + 1, n - 1);
            else if (p > k) p = partition(nums, 0, p - 1);
        }
        return nums[k];
    }

    private int partition(int[] nums, int begin, int end) {
        if (begin == end) return begin;
        int i = begin, j = end - 1, last = nums[end];
        while (i < j) {
            while (i < j && nums[i] >= last) i++;
            while (i < j && nums[j] <= last) j--;
            if (i < j) swap(nums, i, j);
        }
        if (nums[i] < last) {
            swap(nums, i, end);
            return i;
        } else if (nums[i] >= last) {
            swap(nums, i + 1, end);
            return i + 1;
        }
        return i;
    }

    private void randomize(int[] nums) {
        final Random ran = new Random();
        for (int i = 0; i < nums.length; i++) {
            final int r = ran.nextInt(i+1);
            swap(nums, i, r);
        }
    }

    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
