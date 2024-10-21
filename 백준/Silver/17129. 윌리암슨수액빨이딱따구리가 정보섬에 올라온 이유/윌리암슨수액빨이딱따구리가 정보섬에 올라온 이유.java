import java.io.*;
import java.util.*;


public class Main {
    static int[] delta_row = {-1, 1, 0, 0};
    static int[] delta_col = {0, 0, -1, 1};

    private static class Pos {
        int row;
        int col;
        int count;

        Pos(int row, int col, int count) {
            this.row = row;
            this.col = col;
            this.count = count;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int n, m;
        tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());

        int[][] map = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        int start_row = 0, start_col = 0;
        for (int i = 0; i < n; ++i) {
            String line = reader.readLine();
            for (int j = 0; j < m; ++j) {
                map[i][j] = line.charAt(j) - '0';
                if (map[i][j] == 2) {
                    start_row = i;
                    start_col = j;
                    visited[start_row][start_col] = true;
                }
            }
        }

        Pos position;
        Deque<Pos> queue = new ArrayDeque<>();
        queue.add(new Pos(start_row, start_col, 0));
        while (queue.isEmpty() == false) {
            position = queue.poll();
            int next_row, next_col;
            for (int i = 0; i < 4; ++i) {
                next_row = position.row + delta_row[i];
                next_col = position.col + delta_col[i];
                if (0 <= next_row && next_row < n && 0 <= next_col && next_col < m) {
                    if (visited[next_row][next_col] == false) {
                        if (map[next_row][next_col] == 0) {
                            visited[next_row][next_col] = true;
                            queue.add(new Pos(next_row, next_col, position.count + 1));
                        }
                        else if (map[next_row][next_col] != 1) {
                            System.out.println("TAK");
                            System.out.println(position.count + 1);
                            return;
                        }
                    }
                }
            }
        }
        System.out.println("NIE");
    }
}