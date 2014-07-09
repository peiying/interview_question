public class circus {
	public int lis(ArrayList<person> person,int n){
		int k = 1;
		int[] dp = new int[100];
		dp[0] = person.get(0).weight;
		for(int i = 1; i < n; i++){
			if(person.get(i).weight >= dp[k-1]) {
				dp[k++] = person.get(i).weight;
			}else{
				for(int j = k - 1; j >= 0 && dp[j] > person.get(i).weight; j--){
					dp[j+1] = person.get(i).weight;
				}
			}
		}
		return k;
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
