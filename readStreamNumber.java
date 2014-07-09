public class readStreamNumber {
	public static rankNode root = null;
	public static void track(int n){
		if(root == null){
			root = new rankNode(n);
		}else{
			root.insert(n);
		}
	}

	public int getRankOfNumber(int number){
		return root.getRank(number);
		}
    public static void main(String[] args) {

	}
}

class rankNode{
	rankNode left;
	rankNode right;
	int left_size = 0;
	int val = 0;
	public rankNode(int val) {
		this.val = val; 
	}
	public void insert(int n){
		if(n <= val){
			if(left != null) left.insert(val);
			else left = new rankNode(val);
		}else{
			if(right != null) right.insert(val);
			else right = new rankNode(val);
		}
	}
	public int getRank(int n){
		if(n == val){
			return left_size;
		}else if(n < val){
			if(left == null) return -1;
			else return left.getRank(val);
		}else{
			int right_rank = right == null? -1: right.getRank(val);
			if(right_rank == -1) return -1;
			else return left_size + 1 + right_rank;
		}
	}
}
