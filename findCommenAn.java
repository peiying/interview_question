public class findCommenAn {
	public TreeNode findComAn(TreeNode root, TreeNode node1, TreeNode node2){
		if(findNode(root.left, node1)){
			if(findNode(root.right, node2)){
				return root;
			}
			else{
				return findComAn(root.left,node1, node2);
			}
		}else {
				if(findNode(root.left, node2)){
					return root;
				}
				else{
					return findComAn(root.right,node1,node2);
				}
			}
	}
	
	public boolean findNode(TreeNode root, TreeNode tar){
		if(root == null || tar == null) return false;
		if(root == tar) return true;
		boolean found = findNode(root.left, tar);
		if(!found){
			found = findNode(root.right, tar);
		}
		return found;
	}
}
