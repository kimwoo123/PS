import java.io.*;
import java.util.*;


public class Main {
    static int N;
    static int[] matches = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    static boolean finish = false;

    private static void backtrack(int index, int n, int[] result) {
        if (finish == true)
            return;
        if (index == 6) {
            if (n == 0) {
                if ((result[0] * 10) + result[1] + (result[2] * 10) + result[3] == (result[4] * 10) + result[5]) {
                    System.out.print(
                            result[0] + "" + result[1] + "+" + result[2] + "" + result[3] + "=" + result[4] + "" + result[5]
                    );
                    finish = true;
                }
            }
            return;
        }
        for (int i = 0; i < 10; ++i) {
            if (n >= matches[i]) {
                result[index] = i;
                backtrack(index + 1, n - matches[i], result);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(reader.readLine());
        N -= 4;
        if (N < 12) {
            System.out.print("impossible");
            return;
        }

        backtrack(0, N, new int[6]);
        if (finish == false)
            System.out.print("impossible");
    }
}
