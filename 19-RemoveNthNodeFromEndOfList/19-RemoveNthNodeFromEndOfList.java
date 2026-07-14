// Last updated: 7/14/2026, 2:06:06 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode current=head;
        int len=0;
        while (current!=null){
            len++;
            current=current.next;
        }
        if (n == len) {
            return head.next;
        }
        ListNode start=head;
        for(int i=0;i<len-n-1;i++){
                start=start.next;
        }start.next=start.next.next;
        return head;
    } 
}