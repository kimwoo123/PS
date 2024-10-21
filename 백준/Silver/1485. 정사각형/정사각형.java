import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static class Edge {
        int a;
        int b;

        Edge(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    public static double getDistance(Edge j, Edge k) {
        int delta_row = Math.abs(j.a - k.a);
        int delta_col = Math.abs(j.b - k.b);
        return  Math.sqrt(Math.pow(delta_col, 2) + Math.pow(delta_row, 2));
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        Integer T = Integer.parseInt(reader.readLine());
        for (int i = 0; i < T; ++i) {

            Integer a, b;
            Edge[] edges = new Edge[4];
            for (int j = 0; j < 4; ++j) {
                tokenizer = new StringTokenizer(reader.readLine());
                a = Integer.parseInt(tokenizer.nextToken());
                b = Integer.parseInt(tokenizer.nextToken());

                edges[j] = new Edge(a, b);
            }

            Double[] distances = new Double[6];
            int index = 0;
            for (int j = 0; j < 4; ++j) {
                for (int k = 0; k < j; ++k) {
                    if (j == k) continue;
                    distances[index] = getDistance(edges[j], edges[k]);
                    index++;
                }
            }

            Arrays.sort(distances);
            if (Objects.equals(distances[0], distances[1]) && Objects.equals(distances[0], distances[2]) && Objects.equals(distances[0], distances[3]) && Objects.equals(distances[4], distances[5]))
                System.out.println(1);
            else
                System.out.println(0);
        }
    }
}