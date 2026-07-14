// Last updated: 7/14/2026, 2:03:59 PM
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
    public ListNode removeElements(ListNode head, int val) {
        ListNode pre= new ListNode(0);
        pre.next=head;
        ListNode curr=pre;
        while(curr.next!=null){
            if(curr.next.val==val){
                if(curr.next.next==null){
                    curr.next=null;
                }else{
                    curr.next=curr.next.next;
                }
            }else{
                curr=curr.next;
            }
        }return pre.next;
        
    }
}