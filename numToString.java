public class numToString {
	public static String[] digits = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	public static String[] teens = {"eleven", "twelve", "thirteen","fourteen","fifteen","sixteen", "seventeen", "eighteen", "nighteen"};
	public static String[] tens = {"Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Nighty"};
	public static String[] bigs = {"", "Thousand", "Million"};
	public String numberToString(int number){
		String res = "";
		int count = 0;
		while(number > 0){
			if(number % 1000 != 0){
				res = numberTo100(number % 1000) + " " + bigs[count] + " " + res;
			}
			number /= 1000;
			count++;
		}
		return res;
	}
	public String numberTo100(int number){
		String res = "";
		if(number >= 100){
			res += digits[number/100-1] + " hundred ";
			number %= 100;
		}
		if(number >= 11 && number < 20){
			res += teens[number - 11] + " ";
		}else if(number == 10 || number >= 20){
			res += tens[number/10-1] + " ";
			number %= 10;
		}
		if(number >= 1 && number <= 9){
			res += digits[number-1] + " ";
		}
		return res;
	}
	
    public static void main(String[] args) {
    	numToString s = new numToString();
    	System.out.println(s.numberToString(19323984));
	}
}
