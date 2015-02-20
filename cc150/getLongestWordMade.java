public class getLongestWordMade {
	public static HashSet<String> set = new HashSet<String>();
	public boolean makeOfWords(String s, int length){
		int len = s.length();
		if(len == 0) return true;
		for(int i = 1; i <= len; i++){
			if(i == length) return false;
			String str =s.substring(0, i);
			if(set.contains(str)){
				System.out.println(str);
				if(makeOfWords(s.substring(i), length)){
					return true;
				}
			}
		}
		return false;
	}
	public void getLongestWord(ArrayList<String> arr){
		for(String a: arr){
    		set.add(a);
    	}
		//System.out.println("test");
		for(int i = 0; i < arr.size(); i++){
			System.out.println(arr.get(i) + " " + arr.get(i).length());
			if(makeOfWords(arr.get(i), arr.get(i).length())){
				
				System.out.println(arr.get(i));
				return;
			}
		}
	}
    public static void main(String[] args) {
    	getLongestWordMade s = new getLongestWordMade();
    	String arr[] = {"test", "tester", "testertest", "testing", 
                "apple", "seattle", "banana",  "batting", "ngcat", 
                "batti","bat", "testingtester", "testbattingcat"};
    	ArrayList<String> ar = new ArrayList<String>();
    	for(String a: arr){
    		ar.add(a);
    	}
    	Collections.sort(ar,new lengthComparator());
    	s.getLongestWord(ar);
	}
}
class lengthComparator implements Comparator<String> {
	public int compare(String s1, String s2) {
		// TODO Auto-generated method stub
		return s2.length() - s1.length();
	}
}
