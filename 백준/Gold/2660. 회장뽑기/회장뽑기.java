import java.io.*;
import java.util.*;


public class Main {
    static ArrayList<ArrayList<Integer>> graph;
    static int minScore = 50;
    static ArrayList<Integer> candidateList = new ArrayList<>();
    static int N;

    private static Integer bfs(Integer start) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(start);

        int[] visited = new int[N+1];
        Arrays.fill(visited, 50);
        visited[start] = 0;

        Integer node, count, max_count = 0;
        while (queue.isEmpty() == false) {
            node = queue.poll();
            for (Integer nextNode: graph.get(node)) {
                count = visited[node] + 1;
                if (visited[nextNode] > count) {
                    visited[nextNode] = count;
                    if (max_count < count) max_count= count;
                    queue.offer(nextNode);
                }
            }
        }

        return max_count;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        N = Integer.parseInt(reader.readLine());
        graph = new ArrayList<ArrayList<Integer>>(N+1);

        for (int i = 0; i < N+1; ++i)
            graph.add(new ArrayList<>());

        int a, b;
        for (;;) {
            tokenizer = new StringTokenizer(reader.readLine());
            a = Integer.parseInt(tokenizer.nextToken());
            b = Integer.parseInt(tokenizer.nextToken());
            if (a == -1 && b == -1) break;

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        Integer score;
        for (int i = 1; i < N+1; ++i) {
            score = bfs(i);
            if (minScore > score) {
                minScore = score;
                candidateList.clear();
                candidateList.add(i);
            }
            else if (minScore == score)
                candidateList.add(i);
        }

        Collections.sort(candidateList);
        System.out.printf("%d %d\n", minScore, candidateList.size());

        for (Integer i: candidateList)
            System.out.printf("%d ", i);
    }
}