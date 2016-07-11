import java.util.Map;
import java.util.TreeMap;

class Interval {
    int start;
    int end;
    Interval() { start = 0; end = 0; }
    Interval(int s, int e) { start = s; end = e; }
}
 
public class MinMeetingRoomsSweep {
    public int minMeetingRooms(Interval[] intervals) {
       Map<Integer, Integer> map = new TreeMap<>();

       for (Interval i : intervals) {
           map.put(i.start, map.getOrDefault(i.start, 0) + 1);
           map.put(i.end, map.getOrDefault(i.end, 0) - 1);
       }
       int rooms = 0;
       int maxRooms = 0;
       for (Integer val : map.values()) {
           rooms += val;
           maxRooms = Math.max(maxRooms, rooms);
       }
       return maxRooms;
    }
}
