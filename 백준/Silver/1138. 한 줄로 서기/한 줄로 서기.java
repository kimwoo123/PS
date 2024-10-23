import java.io.*;
import java.util.*;


public class Main {
    static boolean[] visited;
    static int[] info;
    static int N;

    private static void combination(int index, int len, Stack<Integer> result) {
        if (index == len) {
            int count, target;
            for (int i = 0; i < N; ++i) {
                count = 0;
                target = result.get(i);
                for (int j = 0; j < i; ++j) {
                    if (result.get(j) > target) ++count;
                }

                if (info[target-1] != count) return;
            }

            StringBuilder sb = new StringBuilder();
            for (int i: result)
                sb.append(i).append(" ");
            System.out.print(sb);
        }
        else {
            for (int i = 1; i < len + 1; ++i) {
                if (visited[i] == false) {
                    visited[i] = true;
                    result.add(i);
                    combination(index + 1, len, result);
                    result.pop();
                    visited[i] = false;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        N = Integer.parseInt(reader.readLine());

        info = new int[N];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < N; ++i) {
            info[i] = Integer.parseInt(tokenizer.nextToken());
        }

        visited = new boolean[N+1];
        combination(0, N, new Stack<>());
    }
}