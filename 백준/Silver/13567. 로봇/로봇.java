import java.io.*;
import java.util.*;


public class Main {
    static int M, n, d;
    static String command;
    static int[] deltaRow = {0, -1, 0, 1};
    static int[] deltaCol = {1, 0, -1, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());

        int row = n, col = 0;
        int nextRow, nextCol;
        int dir = 0;
        for (int i = 0; i < M; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            command = tokenizer.nextToken();
            d = Integer.parseInt(tokenizer.nextToken());

            if (command.equals("MOVE")) {
                nextRow = row + (deltaRow[dir] * d);
                nextCol = col + (deltaCol[dir] * d);
                if (0 <= nextRow && nextRow <= n && 0 <= nextCol && nextCol <= n) {
                    row = nextRow;
                    col = nextCol;
                } else {
                    System.out.print(-1);
                    return;
                }
            } else {
                if (d == 0) {
                    dir = (dir + 1) % 4;
                } else {
                    dir = (dir - 1 + 4) % 4;
                }
            }
        }

        System.out.print(col + " " + (n - row));
    }
}
