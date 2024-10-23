import java.io.*;
import java.util.*;


public class Main {
    static int[] info;
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        N = Integer.parseInt(reader.readLine());

        info = new int[N];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < N; ++i) {
            info[i] = Integer.parseInt(tokenizer.nextToken());
        }

        int[] result = new int[N];
        int count;
        for (int i = 0; i < N; ++i) {
            count = 0;
            for (int j = 0; j < N; ++j) {
                if (count == info[i] && result[j] == 0) {
                    result[j] = i+1;
                    break;
                }
                else if (result[j] == 0)
                    ++count;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; ++i)
            sb.append(result[i]).append(" ");

        System.out.print(sb);
    }
}