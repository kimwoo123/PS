import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] tickets;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        N = Integer.parseInt(reader.readLine());

        tokenizer = new StringTokenizer(reader.readLine());
        tickets = new int[N];
        for (int i = 0; i < N; ++i)
            tickets[i] = Integer.parseInt(tokenizer.nextToken());

        int order = 1;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < N; ++i) {
            while (stack.isEmpty() == false && stack.peek() < tickets[i]) {
                if (order != stack.pop()) {
                    System.out.print("Sad");
                    return;
                }
                ++order;
            }
            stack.add(tickets[i]);
        }

        System.out.print("Nice");
    }
}
