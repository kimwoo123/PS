import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        char[][] str_list = new char[5][15];
        Integer max_len = 0;
        String temp;
        for (int i = 0; i < 5; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            temp = tokenizer.nextToken();
            for (int j = 0; j < temp.length(); ++j)
                str_list[i][j] = temp.charAt(j);

            if (max_len < temp.length())
                max_len = temp.length();
        }

        for (int i = 0; i < max_len; ++i) {
            for (int j = 0; j < 5; ++j) {
                if (str_list[j][i] == '\0') continue;
                System.out.print(str_list[j][i]);
            }
        }

    }
}