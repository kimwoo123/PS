import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int prev, cur;
        prev = -1_000_001;
        tokenizer = new StringTokenizer(reader.readLine());
        while (tokenizer.hasMoreTokens() == true) {
            cur = Integer.parseInt(tokenizer.nextToken());
            if (prev > cur) {
                System.out.print("Bad");
                return;
            }

            prev = cur;
        }

        System.out.print("Good");
    }
}
