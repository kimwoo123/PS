import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static int M;
    static String paper;
    static Vector<BigInteger> result;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        result = new Vector<>();
        M = Integer.parseInt(reader.readLine());
        boolean flag;
        StringBuilder temp;
        for (int i = 0; i < M; ++i) {
            paper = reader.readLine();
            flag = false;
            temp = new StringBuilder();
            for (int j = 0; j < paper.length(); ++j) {
                if ('0' <= paper.charAt(j) && paper.charAt(j) <= '9') {
                    flag = true;
                    temp.append(paper.charAt(j) - '0');
                } else {
                    if (flag == true)
                        result.add(new BigInteger(temp.toString()));
                    temp = new StringBuilder();
                    flag = false;
                }
            }
            if (flag == true)
                result.add(new BigInteger(temp.toString()));
        }

        Collections.sort(result);

        builder = new StringBuilder();
        for (BigInteger i : result) {
            builder.append(i + "\n");
        }

        builder.deleteCharAt(builder.length() -1 );
        System.out.print(builder);
    }
}
