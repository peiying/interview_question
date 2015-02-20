public class findSumInPath {
	public void findSum(int level, int[] path, int sum, TreeNode root){
		if(root == null) return;
		path[level] = root.val;
		int temp = 0;
		for(int i = level; i >= 0; i--){
			temp += path[i];
			if(sum == temp){
				print(level,i,path);
			}
		}
		findSum(level+1, path, sum, root.left);
		findSum(level+1, path, sum, root.right);
	}
	public void print(int start, int end, int[] path){
		for(int i = start; i <= end; i++){
			System.out.println(path[i] + " ");
		}
		System.out.println();
	}
	
	public int getDepth(TreeNode root){
		if(root == null) return 0;
		
		int left = getDepth(root.left);
		int right = getDepth(root.right);
		
		return Math.max(left, right)+1;
	}
}
