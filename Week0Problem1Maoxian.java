import java.util.Arrays;

public class Week0Problem1Maoxian {
	public static void main(String[] args) {
		int[] nums = {3,8, 10};
		int x = 2;
		System.out.println(method(x, nums));
	}
	public static int method(int x, int[] array) {
		Arrays.sort(array);
		int sum = 0;
		for (int i = 0; i <array.length; i++) {
			sum += array[i];
			if (sum == x) {
				return i+1; 
			} else if (sum > x) {
				return i;
			}
		}
		
		return array.length;
	}
}
