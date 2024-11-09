import java.io.*;
import java.util.*;


public class Main {
    static int B, C, D;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        B = Integer.parseInt(tokenizer.nextToken());
        C = Integer.parseInt(tokenizer.nextToken());
        D = Integer.parseInt(tokenizer.nextToken());

        int total = 0;

        int cost;
        int[] hamburgerList = new int[B];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < B; ++i) {
            cost = Integer.parseInt(tokenizer.nextToken());
            hamburgerList[i] = cost;
            total += cost;
        }

        int[] sideList = new int[C];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < C; ++i) {
            cost = Integer.parseInt(tokenizer.nextToken());
            sideList[i] = cost;
            total += cost;
        }

        int[] drinkList = new int[D];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < D; ++i) {
            cost = Integer.parseInt(tokenizer.nextToken());
            drinkList[i] = cost;
            total += cost;
        }

        Arrays.sort(hamburgerList);
        Arrays.sort(sideList);
        Arrays.sort(drinkList);

        int setCount = Math.min(Math.min(B, C), D);
        int discount = 0;
        for (int i = 0; i < setCount; ++i) {
            discount += hamburgerList[hamburgerList.length - i - 1];
            discount += sideList[sideList.length - i - 1];
            discount += drinkList[drinkList.length - i - 1];
        }

        discount = discount / 10;
        System.out.println(total);
        System.out.print(total - discount);
    }
}
