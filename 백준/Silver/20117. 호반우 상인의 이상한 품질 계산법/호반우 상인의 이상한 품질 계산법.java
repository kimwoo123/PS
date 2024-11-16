import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] list;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        N = Integer.parseInt(reader.readLine());
        list = new int[N];

        tokenizer = new StringTokenizer(reader.readLine());
        int a;
        for (int i = 0; i < N; ++i) {
            a = Integer.parseInt(tokenizer.nextToken());
            list[i] = a;
        }

        Arrays.sort(list);

        int total = 0;
        for (int i = N-1; i > N/2; --i) {
            total += list[i] * 2;
        }

        if (N%2 == 1)
            total += list[N/2];
        else
            total += list[N/2] * 2;

        System.out.print(total);
    }
}
