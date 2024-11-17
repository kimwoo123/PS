import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] A;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        N = Integer.parseInt(reader.readLine());

        A = new int[N];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < N; ++i) {
            A[i] = Integer.parseInt(tokenizer.nextToken());
        }

        int[] DP = new int[N];
        Arrays.fill(DP, 1000);
        DP[0] = 0;

        for (int i = 0; i < N; ++i) {
            for (int j = 1; j <= A[i]; ++j) {
                if (i+j == N)
                    break;
                DP[i+j] = Math.min(DP[i] + 1, DP[i+j]);
            }
        }

        if (DP[N-1] == 1000)
            System.out.print(-1);
        else
            System.out.print(DP[N-1]);
    }
}
