import java.io.*;
import java.util.*;


public class Main {
    static int N, E, K;
    static int count, number;
    static int[] people, camp;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        N = Integer.parseInt(reader.readLine());
        E = Integer.parseInt(reader.readLine());

        count = 0;
        people = new int [N+1];
        for (int i = 0; i < E; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            K = Integer.parseInt(tokenizer.nextToken());

            camp = new int[K];
            boolean flag = false;
            int maxValue = 0;
            for (int j = 0; j < K; ++j) {
                camp[j] = Integer.parseInt(tokenizer.nextToken());
                if (camp[j] == 1)
                    flag = true;
                if (people[camp[j]] > maxValue) maxValue = people[camp[j]];
            }

            if (flag == true) {
                for (int j = 0; j < K; ++j) {
                    people[camp[j]] += 1;
                }
            }
            else {
                maxValue = Math.max(maxValue, people[1]);
                for (int j = 0; j < K; ++j) {
                    people[camp[j]] = maxValue;
                }
            }
        }

        builder = new StringBuilder();
        builder.append(1);
        for (int i = 2; i < N+1; ++i) {
            if (people[i] == people[1])
                builder.append("\n" + i);
        }

        System.out.print(builder);
    }
}
