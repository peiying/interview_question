public class circus {
	public int lis(ArrayList<person> person,int n){
		int len = 1;
		int[] dp = new int[100];
		for(int i = 0; i < n; i++){
			dp[i] = 1;
				for(int j = 0; j < i; j++){
					if(person.get(j).weight <= person.get(i).weight && dp[j] + 1 > dp[i]){
						dp[i] = dp[j] + 1;
					}
					if(dp[i] > len) len = dp[i];
				}
		}
		return len;
	}
	
    public static void main(String[] args) {
    	circus s = new circus();
    	ArrayList<person> arr = new ArrayList<person>();
    	arr.add(new person(90,100));
    	arr.add(new person(91,99));
    	arr.add(new person(93,88));
    	arr.add(new person(88,77));
    	Collections.sort(arr,new intervalComparator());
    	for(int i = 0; i < arr.size(); i++){
    		System.out.println(arr.get(i).height + " " + arr.get(i).weight);
    	}
    	System.out.println(s.lis(arr, 4));
	}
}
class person{
	int height;
	int weight;
	public person(int height, int weight) {
		this.height = height;
		this.weight = weight;
	}
	
}
class intervalComparator implements Comparator<person> {
    public int compare(person i1, person i2){
        return i1.height - i2.height;
    }
}
