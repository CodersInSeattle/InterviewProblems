import java.util.PriorityQueue;


class FindMedianFromDataStream {

    private Queue<Integer> minHeap = new PriorityQueue<Integer>();
    private Queue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());

    // Adds a number into the data structure.
    public void addNum(int num) {
        if (maxHeap.size() == minHeap.size()) {
            if (minHeap.size() > 0 && num > minHeap.peek()) {
                int minHead = minHeap.poll();
                maxHeap.add(minHead);
                minHeap.add(num);
            } else
                maxHeap.add(num);
        } else {
            if (num < maxHeap.peek()) {
                int maxHead = maxHeap.poll();
                maxHeap.add(num);
                minHeap.add(maxHead);
            } else
                minHeap.add(num);
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (maxHeap.size() == 0) return 0;
        if (minHeap.size() == maxHeap.size())
            return (minHeap.peek() + maxHeap.peek()) / 2.0;
        else
            return maxHeap.peek();
    }
}
