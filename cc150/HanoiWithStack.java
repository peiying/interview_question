public class HanoiWithStack {
	public void hanoi(int n, char src, char bri, char dst){
		Stack<st> stack = new Stack<st>();
		st temp;
		stack.push(new st(1,n,src,bri,dst));
		while(!stack.isEmpty()){
			temp = stack.pop();
			if(temp.begin != temp.end){
				stack.push(new st(temp.begin, temp.end-1, temp.bri, temp.src, temp.dst));
				stack.push(new st(temp.end, temp.end, temp.src, temp.bri, temp.dst));
				stack.push(new st(temp.begin, temp.end-1, temp.src, temp.dst, temp.bri));
			}else{
				System.out.println("Move Dist" + temp.begin + " from " + temp.src + " to " + temp.dst);
			}
		}
	}
    public static void main(String[] args) {
    	
    	HanoiWithStack s1 = new HanoiWithStack();
    	s1.hanoi(3, 'A', 'B', 'C');
	}
}
