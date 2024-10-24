import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        int A, B, N;
        tokenizer = new StringTokenizer(reader.readLine());
        A = Integer.parseInt(tokenizer.nextToken());
        B = Integer.parseInt(tokenizer.nextToken());
        N = Integer.parseInt(tokenizer.nextToken());

        int result;
        while (N-- > 0)
            A = (A % B) * 10;

        result = A / B;
        System.out.println(result);
    }
}