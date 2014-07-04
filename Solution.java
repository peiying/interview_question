public class Solution {
	public void hanoi(int n, char src, char bri, char dst){
		if(n == 1){
			System.out.println("Move Disk" + n + "from" + src + "to" + "dist");
		}
		else{
			hanoi(n-1, src, bri, dst);
			System.out.println("Move Disk" + n + "from" + src + "to" + "dist");
			hanoi(n-1, bri, src, dst);
		}
	}
    public static void main(String[] args) {
    	
    	Solution s1 = new Solution();
    	s1.hanoi(3, 'A', 'B', 'C');
	}
}
