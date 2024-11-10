import java.io.*;
import java.util.*;


public class Main {
    static int T, N;
    static String line;

    private static int calculateDistance(String a, String b, String c) {
        int result = 0;
        for (int i = 0; i < 4; ++i) {
            if (a.charAt(i) != b.charAt(i))
                ++result;
            if (b.charAt(i) != c.charAt(i))
                ++result;
            if (a.charAt(i) != c.charAt(i))
                ++result;
        }

        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        T = Integer.parseInt(reader.readLine());
        String mbti;
        while (T-- > 0) {
            HashMap<String, Integer> map = new HashMap<>();

            N = Integer.parseInt(reader.readLine());
            tokenizer = new StringTokenizer(reader.readLine());
            for (int i = 0; i < N; ++i) {
                mbti = tokenizer.nextToken();
                map.put(mbti, map.getOrDefault(mbti, 0) + 1);
            }

            int minDistance = 100000;
            int distance;
            for (String i : map.keySet()) {
                map.put(i, map.get(i) - 1);
                for (String j : map.keySet()) {
                    if (map.get(j) == 0)
                        continue;
                    map.put(j, map.get(j) - 1);
                    for (String k : map.keySet()) {
                        if (map.get(k) == 0)
                            continue;
                        map.put(k, map.get(k) - 1);

                        distance = calculateDistance(i, j, k);
                        if (minDistance > distance)
                            minDistance = distance;

                        map.put(k, map.get(k) + 1);
                    }
                    map.put(j, map.get(j) + 1);
                }
                map.put(i, map.get(i) + 1);
            }

            if (minDistance == 100000)
                builder.append(0 + "\n");
            else
                builder.append(minDistance + "\n");
        }

        builder.deleteCharAt(builder.length() - 1);
        System.out.print(builder);
    }
}
