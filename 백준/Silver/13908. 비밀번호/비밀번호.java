import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    static int count;
    static int n, m;

    private static void dfs(boolean[] visited, int index, int use) {
        if (index == n) {
            if (use == m)
                count++;
            return;
        }
        for (int i = 0; i < 10; ++i) {
            if (visited[i] == true) {
                visited[i] = false;
                dfs(visited, index + 1, use + 1);
                visited[i] = true;
            }
            else
                dfs(visited, index + 1, use);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());

        if (m != 0)
            tokenizer = new StringTokenizer(reader.readLine());
        boolean[] visited = new boolean[10];
        int num;
        for (int i = 0; i < m; ++i) {
            num = Integer.parseInt(tokenizer.nextToken());
            visited[num] = true;
        }

        dfs(visited, 0, 0);
        System.out.println(count);
    }
}