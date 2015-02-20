public class SortStack {
	public Stack<Integer> sort(Stack<Integer> s1){
		Stack<Integer> s2 = new Stack<Integer>();
		while(!s1.isEmpty()){
			if(s2.isEmpty()){
				s2.push(s1.pop());
			}else{
				int temp = s1.pop();
				while(temp <= s2.peek()){
					s1.push(s2.pop());
				}
				s2.push(temp);
			}
		}
		return s2;
	}
	
    public static void main(String[] args) {
    	Stack<Integer> s1 = new Stack<Integer>();
    	SortStack s = new SortStack();
    	s1.add(3);
    	s1.add(4);
    	s1.add(5);
    	s1.add(2);
    	s1.add(1);
    	Stack<Integer> s2 = s.sort(s1);
    	while(!s2.isEmpty()){
    		System.out.println(s2.pop());
    	}
	}
}
