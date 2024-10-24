import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;


        HashMap<Integer, Integer> map = new HashMap<>();
        int N = Integer.parseInt(reader.readLine());
        int[] aList = new int[N];
        int a, l;
        for (int i = 0; i < N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            a = Integer.parseInt(tokenizer.nextToken());
            l = Integer.parseInt(tokenizer.nextToken());

            aList[i] = a;
            map.put(a, l);
        }

        Arrays.sort(aList);

        int result = 0;
        int before = 0;
        for (int i = 0; i < N; ++i) {
            if (aList[i] > before)
                ++result;
            before = aList[i] + map.get(aList[i]);
        }

        System.out.println(result);
    }
}