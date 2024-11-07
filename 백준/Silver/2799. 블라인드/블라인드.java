import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static int M, N;
    static String[] window;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        M = Integer.parseInt(tokenizer.nextToken());
        N = Integer.parseInt(tokenizer.nextToken());

        int rowLen = (5 * M) + 1;
        window = new String[rowLen];
        for (int i = 0; i < rowLen; ++i) {
            window[i] = reader.readLine();
        }

        int row, col;
        int[] result = new int[5];
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                row = (i * 5) + 1;
                col = (j * 5) + 1;
                for (int k = 0; k < 4; ++k) {
                    if (window[row + k].charAt(col) != '*') {
                        result[k] += 1;
                        break;
                    }
                    if (k == 3)
                        result[4] += 1;
                }
            }
        }

        System.out.print(result[0] + " " + result[1] + " " + result[2] + " " + result[3] + " " + result[4]);
    }
}
