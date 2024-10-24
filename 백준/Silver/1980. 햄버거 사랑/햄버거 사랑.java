import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int n, m, t;
        tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());
        t = Integer.parseInt(tokenizer.nextToken());

        int result, coke, total;
        int maxHamburger = 0;
        int minCola = 10000;
        for (int i = (t / n); i >= 0; --i) {
            for (int j = (t / m); j >= 0; --j) {
                total = (n * i) + (m * j);
                if (total > t) continue;

                if (minCola > t - total) {
                    minCola = t - total;
                    maxHamburger = i + j;
                    continue;
                }
                else if (minCola == t - total && maxHamburger < i + j)
                    maxHamburger = i + j;
            }
        }

        System.out.printf("%d %d", maxHamburger, minCola);
    }
}