import java.io.*;
import java.util.*;


public class Main {
    static int N, M;
    static String name;
    static int power;

    private static String bisect (int target, int[] powerList, HashMap<Integer, String> map) {
        int start = 0;
        int end = N-1;

        int mid;
        while (start < end) {
            mid = (start + end) / 2;
            if (target <= powerList[mid])
                end = mid;
            else
                start = mid + 1;
        }

        return map.get(powerList[start]);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());

        int before = -1;
        int power;
        int[] powerList = new int[N];
        HashMap<Integer, String> map = new HashMap<>();
        for (int i = 0; i < N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            name = tokenizer.nextToken();
            power = Integer.parseInt(tokenizer.nextToken());

            powerList[i] = power;
            if (before != power)
                map.put(power, name);
            before = power;
        }

        for (int i = 0; i < M; ++i) {
            power = Integer.parseInt(reader.readLine());
            builder.append(bisect(power, powerList, map)).append("\n");
        }

        builder.deleteCharAt(builder.length() - 1);
        System.out.print(builder);
    }
}
