public class Solution {
	public void hanoi(int n, char src, char bri, char dst){
		if(n == 1){
			System.out.println("Move Disk " + n + " from " + src + " to " + dst);
		}
		else{
			hanoi(n-1, src, dst, bri);
			System.out.println("Move Disk " + n + " from " + src + " to " + dst);
			hanoi(n-1, bri, src, dst);
		}
	}
    public static void main(String[] args) {
    	
    	Solution s1 = new Solution();
    	s1.hanoi(3, 'A', 'B', 'C');
	}
}
