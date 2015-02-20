public class MyQueue {
	Stack<Integer> s1 = new Stack<Integer>();
	Stack<Integer> s2 = new Stack<Integer>();
	public void add(int value){
		s1.push(value);
	}
	public int size(){
		return s1.size() + s2.size();
	}
	public int peek(){
		if(s2.isEmpty()){
			shift();
		}
		return s2.peek();
	}
	public int remove(){
		if(s2.isEmpty()){
			shift();
		}
		return s2.pop();
	}
	public boolean isEmpty(){
		return s1.isEmpty() && s2.isEmpty();
	}
	private void shift(){
		while(!s1.isEmpty()){
			s2.push(s1.pop());
		}
	}
    public static void main(String[] args) {
    	
    	MyQueue s = new MyQueue();
    	s.add(5);
    	s.add(4);
    	s.add(3);
    	s.add(2);
    	s.add(1);
    	while(!s.isEmpty()){
    		System.out.println(s.remove());
    	}
	}
