import java.io.*;
import java.util.*;


public class Main {
    static int maxValue;
    static int maxCost;

    private static void greedy(int[] P, int M, int N) {
        int total, count;
        for (int cost: P) {
            count = Math.min(M--, N);
            total = cost * count;
            if (total > maxCost) {
                maxCost = total;
                maxValue = cost;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int N, M;
        tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());

        int[] P = new int[M];
        for (int i = 0; i < M; ++i) {
            P[i] = Integer.parseInt(reader.readLine());
        }

        Arrays.sort(P);
        greedy(P, M, N);

        System.out.printf("%d %d", maxValue, maxCost);
    }
}