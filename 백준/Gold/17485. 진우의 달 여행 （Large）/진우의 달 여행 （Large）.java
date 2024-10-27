import java.io.*;
import java.util.*;


public class Main {

    static int N, M;
    static int[][] graph;
    static int[][][] dp;
    static int[] delta = {-1, 0, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());

        graph = new int[N][M];
        for (int i = 0; i < N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 0; j < M; ++j) {
                graph[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        int deltaCol;
        dp = new int[N][M][3];

        for (int j = 0; j < M; ++j) {
            for (int k = 0; k < 3; ++k) {
                dp[0][j][k] = graph[0][j];
            }
        }

        int minValue;
        for (int i = 1; i < N; ++i) {
            for (int j = 0; j < M; ++ j) {
                for (int k = 0; k < 3; ++k) {
                    minValue = 999999;
                    for (int l = 0; l < 3; ++l) {
                        if (l == delta[k] + 1) continue;
                        if (0 <= j + delta[k] && j + delta[k] < M) {
                            if (minValue > graph[i][j] + dp[i-1][j+delta[k]][l])
                                minValue = graph[i][j] + dp[i - 1][j + delta[k]][l];
                        }
                    }
                    dp[i][j][k] = minValue;
                }
            }
        }

        int result = 999999;
        for (int j = 0; j < M; ++j) {
            for (int k = 0; k < 3; ++k) {
                if (result > dp[N-1][j][k])
                    result = dp[N-1][j][k];
            }
        }

        System.out.print(result);
    }
}