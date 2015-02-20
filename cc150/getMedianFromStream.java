public class getMedianFromStream {
	static PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
	static PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(1, new PQsort());
	public void insertNumber(int randomNumber){
		if(minHeap.size() == maxHeap.size()){
			if(minHeap.peek() != null && randomNumber > minHeap.peek()){
				maxHeap.offer(minHeap.poll());
				minHeap.offer(randomNumber);
			}else{
				maxHeap.offer(randomNumber);
			}
		}else{
			if(randomNumber < maxHeap.peek()){
				minHeap.offer(maxHeap.poll());
				maxHeap.offer(randomNumber);
			}else{
				minHeap.offer(randomNumber);
			}
		}
	}
	public double getMedian( ){
		if(maxHeap.isEmpty()){
			return 0;
		}
		if(minHeap.size() == maxHeap.size()){
			return ((double)minHeap.peek() + (double)maxHeap.peek()) / 2;
		}else{
			return maxHeap.peek();
		}
	}

    public static void main(String[] args) {
    getMedianFromStream s = new getMedianFromStream();
		s.insertNumber(20);
		s.insertNumber(5);
		s.insertNumber(3);
		s.insertNumber(6);
		System.out.println("min: " + minHeap);
		System.out.println("max: " + maxHeap);
		
		System.out.println("median: " + s.getMedian());
	}
}
class PQsort implements Comparator<Integer> {
	 
	public int compare(Integer one, Integer two) {
		return two - one;
	}
}
