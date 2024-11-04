import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static int a, b, c;
    static int N;
    static int i, j, k, r;
    static int[] result;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        tokenizer = new StringTokenizer(reader.readLine());
        a = Integer.parseInt(tokenizer.nextToken());
        b = Integer.parseInt(tokenizer.nextToken());
        c = Integer.parseInt(tokenizer.nextToken());

        result = new int[a+b+c];
        for (int i = 0; i < a+b+c; ++i) {
            result[i] = 2;
        }

        HashSet<Integer[]> pending = new HashSet<>();
        N = Integer.parseInt(reader.readLine());
        for (int t = 0; t < N; ++t) {
            tokenizer = new StringTokenizer(reader.readLine());
            i = Integer.parseInt(tokenizer.nextToken())-1;
            j = Integer.parseInt(tokenizer.nextToken())-1;
            k = Integer.parseInt(tokenizer.nextToken())-1;
            r = Integer.parseInt(tokenizer.nextToken());

            if (r == 1) {
                result[i] = result[j] = result[k] = 1;
            } else {
                pending.add(new Integer[] {i, j, k});
            }
        }

        for (Integer[] each : pending) {
            i = each[0];
            j = each[1];
            k = each[2];
            if (result[i] == 1 && result[j] == 1) {
                result[k] = 0;
            } else if (result[j] == 1 && result[k] == 1) {
                result[i] = 0;
            } else if (result[i] == 1 && result[k] == 1) {
                result[j] = 0;
            }
        }

        builder = new StringBuilder();
        for (int i : result) {
            builder.append(i + "\n");
        }

        builder.deleteCharAt(builder.length()-1);
        System.out.print(builder);
    }
}
