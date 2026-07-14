// Last updated: 7/14/2026, 2:05:22 PM
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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null ||k==0 ){
            return head;
        }
        int len=0;
        ListNode cal=head;
        while(cal!=null){
            len++;
            cal=cal.next;
        }
        int l=k%len;
        if(l==0){
            return head;
        }else{
            for(int i=0;i<l;i++){
                ListNode current=head;
                while(current.next.next!=null){
                    current=current.next;
                }ListNode temp=current.next;
                current.next=null;
                temp.next=head;
                head=temp;
            }
        }
        return head;
    }
}