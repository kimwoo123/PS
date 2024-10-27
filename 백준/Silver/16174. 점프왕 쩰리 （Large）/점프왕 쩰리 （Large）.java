import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int node;
    static int[][] board;
    static boolean[][] visited;
    static int[] deltaRow = {1, 0};
    static int[] deltaCol = {0, 1};

    static class Pos {
        int row;
        int col;

        Pos (int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        N = Integer.parseInt(reader.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 0; j < N; ++j) {
                node = Integer.parseInt(tokenizer.nextToken());
                board[i][j] = node;
            }
        }

        visited = new boolean[N][N];

        Stack<Pos> stack = new Stack<>();
        stack.add(new Pos(0, 0));
        visited[0][0] = true;
        Pos pos;
        int next_row, next_col;
        while (stack.isEmpty() == false) {
            pos = stack.pop();
            if (board[pos.row][pos.col] == 0) continue;
            for (int i = 0; i < 2; ++i) {
                next_row = pos.row + (deltaRow[i] * board[pos.row][pos.col]);
                next_col = pos.col + (deltaCol[i] * board[pos.row][pos.col]);
                if (0 <= next_row && next_row < N && 0 <= next_col && next_col < N) {
                    if (visited[next_row][next_col]) continue;
                    if (board[next_row][next_col] == -1) {
                        System.out.println("HaruHaru");
                        return;
                    }
                    visited[next_row][next_col] = true;
                    stack.add(new Pos(next_row, next_col));
                }
            }
        }

        System.out.println("Hing");
    }
}
