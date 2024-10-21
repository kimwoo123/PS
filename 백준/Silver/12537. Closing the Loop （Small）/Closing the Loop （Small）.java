import java.io.*;
import java.util.*;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        Integer T = Integer.parseInt(reader.readLine());

        Integer N;
        for (int i = 0; i < T; ++i) {
            N = Integer.parseInt(reader.readLine());
            tokenizer = new StringTokenizer(reader.readLine());

            String token, len, color;
            ArrayList<Integer> red_list = new ArrayList<>();
            ArrayList<Integer> blue_list = new ArrayList<>();
            for (int j = 0; j < N; ++j) {
                token = tokenizer.nextToken();
                len = token.substring(0, token.length() - 1);
                color = token.substring((token.length() - 1));

                if (color.equals("R")) red_list.add(Integer.parseInt((len)));
                else blue_list.add(Integer.parseInt(len));
            }

            Collections.sort(blue_list, Collections.reverseOrder());
            Collections.sort(red_list, Collections.reverseOrder());

            Integer total = 0;
            Integer size = Math.min(red_list.size(), blue_list.size());
            for (int k = 0; k < size; ++k) {
                total += blue_list.get(k) + red_list.get(k);
                total -= 2;
            }

            if (total < 0) total = 0;

            System.out.printf("Case #%d: %d\n", i + 1, total);

        }
    }
}