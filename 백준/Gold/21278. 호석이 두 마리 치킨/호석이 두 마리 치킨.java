import java.io.*;
import java.util.*;


public class Main {
    static int N, M;
    static int[][] graph;
    static int minTotal = 500;
    static int[] building = new int[2];
    static int[] result = new int[2];

    private static void choice(int index, int prev) {
        if (index == 2) {
            int total = 0;
            for (int i = 1; i < N+1; ++i) {
                total += Math.min(graph[i][building[0]], graph[i][building[1]]);
//                System.out.print(graph[i][building[0]] + " " + graph[i][building[1]]);
                }
            if (minTotal > total) {
                minTotal = total;
                result = building.clone();
            }
            return;
        }
        for (int i = prev+1; i < N+1; ++i) {
            building[index] = i;
            choice(index+1, i);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());

        graph = new int[N+1][N+1];
        for (int i=0; i<N+1; ++i) {
            Arrays.fill(graph[i], 500);
        }

        for (int i = 0; i <= N; ++i) {
            graph[i][i] = 0;
        }
        
        int a, b;
        for (int i = 0; i < M; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            a = Integer.parseInt(tokenizer.nextToken());
            b = Integer.parseInt(tokenizer.nextToken());

            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        for (int k = 1; k < N+1; ++k) {
            for (int j = 1; j < N+1; ++j) {
                for (int i = 1; i < N+1; ++i) {
                    graph[j][i] = Math.min(graph[j][k] + graph[k][i], graph[j][i]);
                }
            }
        }

        choice(0, 0);
        System.out.print(result[0] + " " + result[1] + " " + (minTotal * 2));
    }
}
