public class findT2InT1 {
	public Boolean isSubTree(TreeNode t1, TreeNode t2){
		if(t1 == null) return false;
		
		else return subTree(t1,t2);
	}
	public Boolean subTree(TreeNode t1, TreeNode t2){
		if(t1 == null) {
			return false;
		}
		else if(t1.val == t2.val){
			if(match(t1,t2)){
				return true;
			}else{
				return false;
			}
		}
		else{
			return subTree(t1.left, t2) || subTree(t1.right, t2);
		}
	}
	public Boolean match(TreeNode t1, TreeNode t2){
		if(t1 == null && t2 == null){
			return true;
		}else if(t1 == null || t2 == null){
			return false;
		}else{
			return match(t1.left, t2.left) && match(t1.right, t2.right);
		}
	}
}
