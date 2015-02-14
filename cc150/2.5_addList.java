public class solution {
	
	public LinkedListNode addList(LinkedListNode l1, LinkedListNode l2){
		if(l1 == null && l2 == null){
			return null;
		}
		
		LinkedListNode newList = new LinkedListNode(0);
		LinkedListNode cur = newList;
		int carry = 0;
		int value = 0;
		while(l1 != null || l2 != null){
			if(l1 != null){
				value += l1.data;
				l1 = l1.next;
			}
			if(l2 != null){
				value += l2.data;
				l2 = l2.next;
			}
			cur.next = new LinkedListNode((value + carry) % 10);
			carry = (value + carry) / 10;
			cur = cur.next;
			value = 0;
		}
		if(carry == 1){
			cur.next = new LinkedListNode(carry);
		}	
		return newList.next;
	}

	public static void main(String[] args) {
		LinkedListNode l1 = new LinkedListNode(7);
		l1.next = new LinkedListNode(1);
		l1.next.next = new LinkedListNode(6);
		LinkedListNode l2 = new LinkedListNode(5);
		l2.next = new LinkedListNode(9);
		l2.next.next = new LinkedListNode(6);
		solution s = new solution();
		LinkedListNode res = s.addList(l1, l2);
		while(res != null){
			System.out.println(res.data);
			res = res.next;
		}
	}
}
class LinkedListNode{
	int data;
	LinkedListNode next;
	public LinkedListNode(int data){this.data = data;}
}
