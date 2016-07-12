public class ReconstructItineraryTreeSet {
    public List<String> findItinerary(String[][] tickets) {
        List<String> ans = new ArrayList<>(tickets.length + 1);
        Map<String, Set<String>> map = new HashMap<>();
        Map<String, Integer> pathMap = new HashMap<>();
        
        for (String[] pair : tickets) {
            Set<String> set = map.get(pair[0]);
            
            if (set == null) {
                set = new TreeSet<>();
                map.put(pair[0], set);
            }
            String path = pair[0] + pair[1];
            Integer count = pathMap.get(path);
            if (count == null) {
                count = 0;
            }
            pathMap.put(path, count + 1);
            set.add(pair[1]);
        }
        ans.add("JFK");
        dfs(ans, map, tickets.length + 1, pathMap);
        return ans;
    }
    boolean dfs(List<String> ans, Map<String, Set<String>> map, int total, Map<String, Integer> pathMap) {
        if (ans.size() == total) {
            return true;
        }
        String curr = ans.get(ans.size() - 1);
        if (map.get(curr) == null) {
            return false;
        }
        for (String next : map.get(curr)) {
            if (ans.size() < total - 1 && map.get(curr) == null) {
                continue;
            }
            String path = curr + next;
            int count = pathMap.get(path);
            if (count > 0) {
                pathMap.put(path, count - 1);
                ans.add(next);
                if (dfs(ans, map, total, pathMap)) {
                    return true;
                } 
                ans.remove(ans.size() - 1);
                pathMap.put(path, count);
            }
        }
        return false;
    }
}
