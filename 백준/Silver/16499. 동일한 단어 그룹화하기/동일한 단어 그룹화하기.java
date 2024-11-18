import java.io.*;
import java.util.*;


public class Main {
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(reader.readLine());

        HashSet<String> set = new HashSet<>();
        String word;
        char[] c;
        int result = 0;
        for (int i=0; i<N; ++i) {
            word = reader.readLine();
            c = word.toCharArray();
            Arrays.sort(c);
            word = String.valueOf(c);
            if (set.contains(word) == false) {
                set.add(word);
                ++result;
            }
        }

        System.out.print(result);
    }
}
