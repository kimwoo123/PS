import java.io.*;
import java.util.*;

class Road {
    int end;
    int weight;

    Road(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }
}
public class Main {
    static ArrayList<ArrayList<Road>> graph;
    static boolean[] visited;
    static final int INF = 987654321;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int TC;
        tokenizer = new StringTokenizer(reader.readLine());
        TC = Integer.parseInt(tokenizer.nextToken());

        for (int i=0; i<TC; ++i) {
            int N, M, W;
            tokenizer = new StringTokenizer(reader.readLine());
            N = Integer.parseInt(tokenizer.nextToken());
            M = Integer.parseInt(tokenizer.nextToken());
            W = Integer.parseInt(tokenizer.nextToken());

            graph = new ArrayList<>(N+1);
            for (int j = 0; j <= N; ++j)
                graph.add(new ArrayList<>());

            int S, E, T;
            for (int j = 0; j < M; ++j) {
                tokenizer = new StringTokenizer(reader.readLine());
                S = Integer.parseInt(tokenizer.nextToken());
                E = Integer.parseInt(tokenizer.nextToken());
                T = Integer.parseInt(tokenizer.nextToken());

                graph.get(S).add(new Road(E, T));
                graph.get(E).add(new Road(S, T));
            }

            for (int j = 0; j < W; ++j) {
                tokenizer = new StringTokenizer(reader.readLine());
                S = Integer.parseInt(tokenizer.nextToken());
                E = Integer.parseInt(tokenizer.nextToken());
                T = Integer.parseInt(tokenizer.nextToken());

                graph.get(S).add(new Road(E, -T));
            }

            boolean result;
            result = bellmanFord(N, M);
            System.out.println(result ? "YES": "NO");
        }
    }

    private static boolean bellmanFord(int V, int E) {
        int[] distance_list = new int[V+1];
        Arrays.fill(distance_list, INF);
        distance_list[1] = 0;

        for (int i = 0; i < V; ++i) {
            for (int j = 1; j <= V; ++j) {
                for (Road r: graph.get(j)) {
                    if (distance_list[j] + r.weight < distance_list[r.end]) {
                        distance_list[r.end] = distance_list[j] + r.weight;
                        if (i == V-1)
                            return true;
                    }
                }
            }
        }

        return false;
    }
}