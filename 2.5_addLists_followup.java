/* addList follow up */
public class solution {
	
	/*create a wrapper class solve this problem*/
	
	public class partialSum{
		public LinkedListNode sum = null;
		public int carry = 0;
	}
	
	public LinkedListNode addLists(LinkedListNode l1, LinkedListNode l2){
		int len1 = lenth(l1);
		int len2 = lenth(l2);
		/* pad the shorter list with zero */
		if(len1 < len2){
			l1 = padZero(l1, len2-len1);
		}else{
			l2 = padZero(l2, len1-len2);
		}
		
		/* add list with a helper function */
		partialSum sum = addListsHelper(l1,l2);
		
		/* check the left carry. if 0, just return the linked list, otherwise insert at front of the list*/
		if(sum.carry == 0){
			return sum.sum;
		}else{
			LinkedListNode result = insertBefore(sum.sum, sum.carry);
			return result;
		}
	}
	
	public partialSum addListsHelper(LinkedListNode l1, LinkedListNode l2) {
		if(l1 == null && l1 == null){
			partialSum sum = new partialSum();
			return sum;
		}
		/* add smaller digit recursively */
		partialSum sum = addListsHelper(l1.next, l2.next);
		/* add carry to current sum*/
		int val = sum.carry + l1.data + l2.data;
		/* insert to before location*/
		LinkedListNode result = insertBefore(sum.sum, val % 10);
		sum.sum = result;
		sum.carry = val / 10;
		return sum;
	}

	public LinkedListNode insertBefore(LinkedListNode list, int data) {
		LinkedListNode n = new LinkedListNode(data);
		if(list != null){
			n.next = list;
		}
		return n;
	}

	public LinkedListNode padZero(LinkedListNode l, int padding) {
		LinkedListNode head = l;
		for(int i = 0; i < padding; i++){
			LinkedListNode n = new LinkedListNode(0);
			n.next = head;
			head = n;
		}
		return head;
	}
	
	public int lenth(LinkedListNode l1) {
		int count = 1;
		while(l1 != null){
			l1 = l1.next;
			count++;
		}
		return count;
	}
	
	public static void main(String[] args) {
		LinkedListNode l1 = new LinkedListNode(7);
		l1.next = new LinkedListNode(1);
		l1.next.next = new LinkedListNode(6);
		LinkedListNode l2 = new LinkedListNode(5);
		l2.next = new LinkedListNode(9);
		//l2.next.next = new LinkedListNode(6);
		solution s = new solution();
		LinkedListNode res = s.addLists(l1, l2);
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
