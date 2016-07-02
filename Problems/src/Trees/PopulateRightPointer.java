/**
 * 116. Populating Next Right Pointers in Each Node 
 *
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class PopulateRightPointer {
    public void connect(TreeLinkNode root) {
        TreeLinkNode levelHead = root;
        
        while (levelHead != null) {
            TreeLinkNode curr = levelHead;
            levelHead = null;
            TreeLinkNode currChild = null;
            TreeLinkNode prevChild = null;
            
            while (curr != null) {
                currChild = curr.left == null ? curr.right : curr.left;
                levelHead = levelHead == null ? currChild : levelHead;
                if (prevChild != null && currChild != null) {
                    prevChild.next = currChild;
                    prevChild = currChild;
                }
                if (curr.left != null && curr.right != null) {
                    curr.left.next = curr.right;
                    prevChild = curr.right;
                }
                curr = curr.next;
            }
        }
    }
}
