import java.io.*;
import java.util.*;


public class Main {
    static int x;
    static int n;
    static int[] blocks;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        String line;
        while ((line = reader.readLine()) != null) {
            x = Integer.parseInt(line) * 10000000;
            n = Integer.parseInt(reader.readLine());

            blocks = new int[n];
            for (int i = 0; i < n; ++i) {
                blocks[i] = Integer.parseInt(reader.readLine());
            }

            Arrays.sort(blocks);

            int start, end, total;
            start = 0;
            end = n - 1;

            boolean flag = false;
            while (start < end) {
                total = blocks[start] + blocks[end];

                if (total == x) {
                    System.out.println("yes " + blocks[start] + " " + blocks[end]);
                    flag = true;
                    break;
                } else if (total > x) {
                    --end;
                } else {
                    ++start;
                }
            }

            if (flag == false)
                System.out.println("danger");
        }
    }
}
