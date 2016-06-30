package Trees;

/**
 * Leetcode 314
 * Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
 * If two nodes are in the same row and column, the order should be from left to right.

 * Examples:
 * Given binary tree [3,9,20,null,null,15,7],
      3
     /\
    /  \
   9   20
       /\
      /  \
     15   7
 * return its vertical order traversal as:
 * [
 * [9],
 * [3,15],
 * [20],
 * [7]
 * ]
 */
public class BinaryTreeVerticalTraversal {

    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList();
        Map<TreeNode, Integer> weights = new HashMap();
        Map<Integer, List<Integer>> levels = new HashMap();

        int minLevel = Integer.MAX_VALUE;
        queue.add(root);
        weights.put(root, 0);

        while (!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            int weight = weights.get(curr);
            minLevel = Math.min(minLevel, weight);

            if (!levels.containsKey(weight)) levels.put(weight, new ArrayList());
            levels.get(weight).add(curr.val);

            if (curr.left != null) {
                queue.add(curr.left);
                weights.put(curr.left, weight - 1);
            }

            if (curr.right != null) {
                queue.add(curr.right);
                weights.put(curr.right, weight + 1);
            }
        }

        while (levels.containsKey(minLevel)) result.add(levels.get(minLevel++));
        return result;
    }
}
