public class FindNextNode {
	public TreeNode findLeft(TreeNode node){
		if(node == null) return null;
		while(node.left != null){
			node = node.left;
		}
		return node;
	}
	
	public TreeNode findNextNode(TreeNode node){
		if(node == null) return null;
		if(node.right != null){
			return findLeft(node.right);
		}
		TreeNode p = node.parent;
		while(p != null && p.right == node){
			node = p;
			p = p.parent;
		}
		return p;
	}
}
