import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static String S;


    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        S = reader.readLine();

        builder = new StringBuilder(S);

        int l, count;
        l = builder.length();
        Stack<Integer> pending = new Stack<>();

        int count1 = 0;
        for (int i = 0; i < l; ++i) {
            if (builder.charAt(i) == '1')
                ++count1;
        }

        int count0 = l - count1;

        // 앞에서 1 빼기
        count = count1 / 2;
        for (int i = 0; i < l; ++i) {
            if (builder.charAt(i) == '1') {
                pending.add(i);
                --count;
                if (count == 0)
                    break;
            }
        }

        int index;
        while (pending.isEmpty() == false) {
            index = pending.pop();
            builder.deleteCharAt(index);
        }

        // 뒤에서 0 빼기
        count = count0 / 2;
        for (int i = builder.length()-1; i > -1; --i) {
            if (builder.charAt(i) == '0') {
                pending.add(i);
                --count;
                if (count == 0)
                    break;
            }
        }

        for (Integer i : pending) {
            builder.deleteCharAt(i);
        }

        System.out.print(builder);
    }
}
