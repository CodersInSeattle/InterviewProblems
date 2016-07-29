public class Solution {
    public String rearrangeString(String str, int k) {
        if (k == 0) {
            return str;
        }
        int count[] = loadCount(str);
        int freeze[] = new int[256];
        PriorityQueue<Character> heap = buildAndFillHeap(count);
        Queue<Character> queue = new LinkedList<>();
        StringBuilder buf = new StringBuilder();
        
        while (heap.size() > 0) {
            char ch = heap.poll();
            buf.append(ch);
            nextStep(freeze, heap, count, queue, ch, k);
        }
        return queue.size() > 0 ? "" : buf.toString();
    }
    private int[] loadCount(String s) {
        int arr[] = new int[256];
        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i)]++;
        }
        return arr;
    }
    private void nextStep(int freeze[], PriorityQueue<Character> heap, int count[], Queue<Character> queue, char ch, int k) {
        if (count[ch] > 1) {
            freeze[ch] = k;
            count[ch]--;
            queue.offer(ch);
        }
        
        while (queue.size() > 0 && freeze[queue.peek()] == 1) {
            heap.offer(queue.poll());
        }
        for (Character idx : queue) {
            freeze[idx]--;
        }
    }
    private PriorityQueue<Character> buildAndFillHeap(final int[] count) {
        PriorityQueue<Character> heap = new PriorityQueue<>((a, b) -> count[b] - count[a]);
        for (char i = 0; i < count.length; i++) {
            if (count[i] > 0) {
                heap.offer(i);
            }
        }
        return heap;
    }
}
