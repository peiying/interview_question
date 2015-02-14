/*
 * This algorithm is best. Runtime is O(N2), space is O(1)
 */

public class solution {
	
	public int[][] rotateMatrix(int[][] matrix, int n){
		
		for(int layer = 0; layer < n/2; layer++){
			int first = layer;
			int last = n - 1 - layer;
			
			for(int i = first; i < last; i++){
				int offset = i - first; // increasing value
				//left-up to temp
				int temp = matrix[first][i];
				//left-down to left-up
				matrix[first][i] = matrix[last - offset][first];
				//right-down to left-down
				matrix[last - offset][first] = matrix[last][last - offset];
				//right-up to right-down
				matrix[last][last - offset] = matrix[i][last];
				//temp to right-up
				matrix[i][last] = temp;
			}
		}
		return matrix;
	}

	public static void main(String[] args) {
		int matrix[][] = { {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
		solution s = new solution();
		int res[][] = s.rotateMatrix(matrix, 4);
		for(int i = 0; i < res.length; i++){
			for(int j = 0; j < res[0].length; j++){
				System.out.print(res[i][j] + " ");
			}
			System.out.println();
		}
	}
}
