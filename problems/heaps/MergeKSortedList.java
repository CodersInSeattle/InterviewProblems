import java.util.PriorityQueue;

class ListNode {
	int val;
	ListNode next;
	ListNode(int x) {
		val = x;
	}
}
public class MergeKSortedList {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> queue = new PriorityQueue<>(
            (l1, l2) -> l1.val - l2.val
        );
        for (ListNode node : lists) {
            if (node != null) {
                queue.offer(node);
            }
        }
        
        ListNode head = new ListNode(-1);
        ListNode tail = head;
        
        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            
            if (node.next != null) {
                queue.offer(node.next);
            }
            tail.next = node;
            tail = tail.next;
        }
        return head.next;
    }
}
