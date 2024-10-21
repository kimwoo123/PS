import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        Integer n = Integer.parseInt(reader.readLine());

        Integer[] card_list = new Integer[n];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; ++i)
            card_list[i] = Integer.parseInt(tokenizer.nextToken());

        Arrays.sort(card_list, Collections.reverseOrder());

        // 음수 2, 양수 2, 음수 2 + 양수 1, 양수 3
        // n-1 n-2, 0 1, n-1 n-2 0, 0 1 2
        Integer a = card_list[n-1] * card_list[n-2];
        Integer b = card_list[0] * card_list[1];
        Integer c = card_list[n-1] * card_list[n-2] * card_list[0];
        Integer d = card_list[0] * card_list[1] * card_list[2];

        Integer result = Math.max(Math.max(a, b), Math.max(c, d));
        System.out.println(result);
    }
}