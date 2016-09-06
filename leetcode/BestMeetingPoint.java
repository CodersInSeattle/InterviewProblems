/*
 * Leet code problem: 296. Best Meeting Point
 *
 * A group of two or more people wants to meet and minimize the total travel distance. 
 * You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
 * The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
 *
 * For example, given three people living at (0,0), (0,4), and (2,2):
 * 
 * The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
 */
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class BestMeetingPoint {
    public int minTotalDistance(int[][] grid) {
        List<Integer> xList = new ArrayList<>() ;
        List<Integer> yList = new ArrayList<>();
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    xList.add(i);
                    yList.add(j);
                }
            }
        }
        return getMin(xList) + getMin(yList);
    }

    private int getMin(List<Integer> list) {
        Collections.sort(list);
        int left = 0;
        int right = list.size() - 1;
        int min = 0;
        while (left < right) {
            min += list.get(right--) - list.get(left++);
        }
        return min;
    }
}
