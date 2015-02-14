public class Solution {
	 public static int[] rerange(int[] A) {
	        int len = A.length;
	        int cntPos = 0, cntNeg = 0;
	        for(int a: A){
	            if(a > 0){
	                cntPos++;
	            }else{
	                cntNeg++;
	            }
	        }
	        int pos = 0, neg = 1;
	        if(cntPos < cntNeg){
	            pos = 1;
	            neg = 0;
	        }
	        while(pos < len && neg < len){
	            while(pos < len && A[pos] > 0) pos += 2;
	            while(neg < len && A[neg] < 0) neg += 2;
	            if(pos < len && neg < len){
	                swap(A, pos, neg);
	                pos += 2;
	                neg += 2;
	            }
	        }
	        return A;
	   }
	   public static void swap(int[] A, int i, int j){
	       int temp = A[i];
	       A[i] = A[j];
	       A[j] = temp;
	   }
	   public static void main(String[] args){
		   int[] a = {-6,-7,1,2,3,4,5};
		   int[] b = rerange(a);
		   for(int s: b) System.out.print(s);
	   }
}
