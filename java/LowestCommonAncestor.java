public class lowestCommonAncestor{
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q){
    if (root == null || p == null || q == null)
      return null;
    return helper(root, p, q);
  }

  private TreeNode helper(TreNode root, TreeNode p, TreeNode q){
    if (root == null || root == p || root == q)
      return root;
    TreeNode left = helper(root.left, p, q);
    TreeNode right = helper(root.right, p, q);

    if(left != null && right != null){
      return root;
    }
    return left == null? right:left;
  }
}
