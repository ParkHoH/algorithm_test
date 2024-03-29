
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		if (N <= 3) {
			if (N == 1)
				System.out.println(0);
            else
				System.out.println(1);
			
		} else {
			int[] dp = new int[N+1];
			Arrays.fill(dp, Integer.MAX_VALUE);
			dp[1] = 0;
			dp[2] = 1;
			dp[3] = 1;
			
			for (int i = 4; i < N+1; i++) {
				if (i % 3 == 0)
					dp[i] = Math.min(dp[i], dp[i/3] + 1);
				
				if (i % 2 == 0)
					dp[i] = Math.min(dp[i], dp[i/2] + 1);
				
				dp[i] = Math.min(dp[i], dp[i-1] + 1);
			}
			
			System.out.println(dp[N]);
		}
	}
}
