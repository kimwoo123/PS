import java.io.*;
import java.util.*;


public class Main {
    static char[] s, result;
    static boolean[] visited;
    static boolean finish;
    static String origin, line, res;
    static int len, count, order;

    private static void backtrack(char[] s, int index) {
        if (finish == true)
            return;
        if (index == len) {
            ++count;
            if (count == order) {
                res = String.valueOf(result);
                finish = true;
            }
            return;
        }

        for (int i = 0; i < len; ++i) {
            if (visited[i] == false) {
                visited[i] = true;
                result[index] = s[i];
                backtrack(s, index+1);
                visited[i] = false;
            }
        }

    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        for (;;) {
            line = reader.readLine();
            if (line == null)
                break;

            tokenizer = new StringTokenizer(line);
            origin = tokenizer.nextToken();
            s = origin.toCharArray();
            Arrays.sort(s);
            order = Integer.parseInt(tokenizer.nextToken());
            len = s.length;
            count = 0;
            finish = false;
            visited = new boolean[len];
            result = new char[len];

            backtrack(s, 0);
            if (finish == true)
                builder.append(origin + " " + order + " = " + res + "\n");
            else
                builder.append(origin + " " + order + " = " + "No permutation" + "\n");

        }

        builder.deleteCharAt(builder.length()-1);
        System.out.print(builder);
    }
}
