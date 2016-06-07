public class SymeticTree{
  public boolean isSymetric(TreeNode root){
    if(root == null)
        return true;
    return isSymetric(root.left, root.right);
    }

  public boolean isSymetric(TreeNode one, TreeNode two){
    if(root == null || two == null){
      if(one == two)
        return true;
      else
        return false;
    }
    if(one.val != two.val){
      return false;
    else
      return isSymeetric(one.left, two.right) && isSymeetric(one.right, two.left);
  }
}
