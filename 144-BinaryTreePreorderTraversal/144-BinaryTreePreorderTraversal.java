// Last updated: 7/14/2026, 2:04:28 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer>res=new ArrayList<>();
        preorder(root,res);
        return res;
    }
    private static void preorder(TreeNode curr,List<Integer> res){
        if(curr==null) return;
        res.add(curr.val);
        preorder(curr.left,res);
        preorder(curr.right,res);
    }
}