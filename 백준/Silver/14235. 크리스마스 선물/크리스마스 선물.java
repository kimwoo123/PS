import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int N = Integer.parseInt(reader.readLine());

        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int a, present;
        for (int i = 0; i < N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            a = Integer.parseInt(tokenizer.nextToken());
            if (a == 0) {
                if (heap.isEmpty())
                    sb.append(-1).append("\n");
                else
                    sb.append(-heap.poll()).append("\n");
            }
            else {
                for (int j = 0; j < a; ++j) {
                    present = Integer.parseInt(tokenizer.nextToken());
                    heap.offer(-present);
                }
            }
        }

        sb.deleteCharAt(sb.length() - 1);
        System.out.print(sb);
    }
}