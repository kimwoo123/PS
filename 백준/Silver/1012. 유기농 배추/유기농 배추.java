import java.io.*;
import java.util.*;


public class Main {
    static int[] delta_row = {-1, 1, 0, 0};
    static int[] delta_col = {0, 0, 1, -1};
    static int M, N, K;

    static class Node {
        int row;
        int col;

        Node(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    private static void floodFill(int[][] board, int[][] visited, int startRow, int startCol) {
        Node node = new Node(startRow, startCol);
        visited[startRow][startCol] = 1;

        ArrayDeque<Node> queue = new ArrayDeque<>();
        queue.offer(node);
        int next_row, next_col;
        while (queue.isEmpty() == false) {
            node = queue.poll();
            for (int i = 0; i < 4; ++i) {
                next_row = node.row + delta_row[i];
                next_col = node.col + delta_col[i];
                if ((0 <= next_row && next_row < N) && (0 <= next_col && next_col < M)) {
                    if (board[next_row][next_col] == 1 && visited[next_row][next_col] == 0) {
                        visited[next_row][next_col] = 1;
                        queue.offer(new Node(next_row, next_col));
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int T = Integer.parseInt(reader.readLine());
        for (int i = 0; i < T; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            N = Integer.parseInt(tokenizer.nextToken());
            M = Integer.parseInt(tokenizer.nextToken());
            K = Integer.parseInt(tokenizer.nextToken());

            int[][] board = new int[N][M];
            int row, col;
            for (int j = 0; j < K; ++j) {
                tokenizer = new StringTokenizer(reader.readLine());
                row = Integer.parseInt(tokenizer.nextToken());
                col = Integer.parseInt(tokenizer.nextToken());
                board[row][col] = 1;
            }

            int count = 0;
            int[][] visited = new int[N][M];
            for (int j = 0; j < N; ++j) {
                for (int k = 0; k < M; ++k) {
                    if (board[j][k] == 1 && visited[j][k] == 0) {
                        floodFill(board, visited, j, k);
                        ++count;
                    }
                }
            }

            System.out.println(count);
        }
    }
}