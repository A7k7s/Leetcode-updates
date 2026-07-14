// Last updated: 7/14/2026, 2:03:40 PM
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
    public boolean isPalindrome(ListNode head) {
        List<Integer> li=new ArrayList();
        while(head!=null){
            li.add(head.val);
            head=head.next;
        }
        int left=0;
        int right=li.size()-1;
        while(left<right&&li.get(left)==li.get(right)){
            left++;
            right--;
        }
        return left>=right;
    }
}