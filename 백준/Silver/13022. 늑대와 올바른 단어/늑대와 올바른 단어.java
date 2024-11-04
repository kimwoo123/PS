import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static String word;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        word = reader.readLine();
        int l = -1;

        char[] spell = new char[] {'w', 'o', 'l', 'f'};
        int order = 0;

        char c;
        int count = 0;
        for (int i = 0; i < word.length(); ++i) {
            c = word.charAt(i);
            if (c == spell[order]) {
                ++count;
            } else if (c == spell[(order+1) % 4]) {
                if (l == -1)
                    l = count;
                else if (l != count) {
                    System.out.print('0');
                    return;
                }
                order = (order+1) % 4;
                if (order == 0)
                    l = -1;
                count = 1;
            } else {
                System.out.print('0');
                return;
            }
        }

         if (order != 3 || (order == 3 && count != l)) {
            System.out.print('0');
            return;
        }
        System.out.print('1');
    }
}
