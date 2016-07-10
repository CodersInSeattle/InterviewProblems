import java.util.Arrays;
import java.util.PriorityQueue;

class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}
 
public class MinMeetingRooms {
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        PriorityQueue<Interval> queue = new PriorityQueue<>((i1, i2) -> i1.end - i2.end);
        Arrays.sort(intervals, (i1, i2) -> i1.start - i2.start);
        
        int count = 0;
        
        for (Interval interval : intervals) {
            while (!queue.isEmpty() && interval.start >= queue.peek().end) {
                queue.poll();
            }
            queue.offer(interval);
            count = Math.max(queue.size(), count);
        }
        return count;
    }
}
