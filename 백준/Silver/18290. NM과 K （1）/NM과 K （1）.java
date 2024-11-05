import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static int N, M, K;
    static int[][] matrix;
    static int[][] visited;
    static int result = -1_000_001;
    static int[] deltaRow = {0, 0, 1, -1};
    static int[] deltaCol = {1, -1, 0, 0};

    private static void visitPos(int row, int col, int flag) {
        int nextRow, nextCol;
        for (int k = 0; k < 4; ++k) {
            nextRow = row + deltaRow[k];
            nextCol = col + deltaCol[k];
            if (0 <= nextRow && nextRow < N && 0 <= nextCol && nextCol < M) {
                visited[nextRow][nextCol] += flag;
            }
        }
    }

    private static void DFS(int index, int sum) {
        if (index == K) {
            if (sum > result)
                result = sum;
            return;
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (visited[i][j] == 0) {
                    visitPos(i, j, 1);
                    visited[i][j] += 1;
                    DFS(index+1, sum + matrix[i][j]);
                    visitPos(i, j, -1);
                    visited[i][j] += -1;
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        tokenizer = new StringTokenizer(reader.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());
        K = Integer.parseInt(tokenizer.nextToken());

        matrix = new int[N][M];
        for (int i = 0; i< N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 0; j < M; ++j) {
                matrix[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        visited = new int[N][M];
        DFS(0, 0);
        System.out.print(result);
    }
}
