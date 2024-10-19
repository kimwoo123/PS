import java.io.*;
import java.util.*;


public class Main {
    static StringBuilder builder = new StringBuilder();
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int N, M, V;
        tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt((tokenizer.nextToken()));
        M = Integer.parseInt((tokenizer.nextToken()));
        V = Integer.parseInt((tokenizer.nextToken()));

        graph = new ArrayList[N+1];
        for (int i = 1; i <= N; ++i)
            graph[i] = new ArrayList<>();

        int x, y;
        for (int i = 0; i < M; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            x = Integer.parseInt(tokenizer.nextToken());
            y = Integer.parseInt(tokenizer.nextToken());
            graph[x].add(y);
            graph[y].add(x);
        }

        for (int i = 1; i <= N; ++i)
            Collections.sort(graph[i]);

        visited = new boolean[N+1];
        dfs(V);

        builder.append('\n');

        visited = new boolean[N+1];
        bfs(V);

        System.out.println(builder);
    }

    private static void dfs(int node) {
        visited[node] = true;
        builder.append(node).append(' ');
        for (int next_node: graph[node]) {
            if (visited[next_node] == false) {
                dfs(next_node);
            }
        }
    }

    private static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        visited[start] = true;
        queue.add(start);

        int node;
        while (queue.isEmpty() == false) {
            node = queue.poll();
            builder.append(node).append(' ');
            for (int next_node: graph[node]) {
                if (visited[next_node] == false) {
                    visited[next_node] = true;
                    queue.add(next_node);
                }
            }
        }
    }
}