import java.io.*;
import java.util.*;


public class Main {
    private static void initHashMap(SortedMap<String, Integer> map) {
        map.put("TTT", 0);
        map.put("TTH", 0);
        map.put("THT", 0);
        map.put("THH", 0);
        map.put("HTT", 0);
        map.put("HTH", 0);
        map.put("HHT", 0);
        map.put("HHH", 0);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        SortedMap<String, Integer> map =  new TreeMap<>(Comparator.reverseOrder());
        int P = Integer.parseInt(reader.readLine());
        String testCase, key;
        while (P-- > 0) {
            initHashMap(map);
            testCase = reader.readLine();
            for (int i = 0; i < testCase.length() - 2; ++i) {
                key = testCase.substring(i, i+3);
                map.put(key, map.get(key) + 1);
            }

            builder = new StringBuilder();
            for (int i : map.values())
                builder.append(i).append(' ');

            builder.deleteCharAt(builder.length()-1);
            builder.append("\n");
            System.out.print(builder);
        }
    }
}