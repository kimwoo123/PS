import java.io.*;
import java.util.*;


public class Main {
        static String line;
        static int m;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder builder = new StringBuilder();

        for (;;) {
            m = Integer.parseInt(reader.readLine());
            if (m == 0)
                break;

            line = reader.readLine();

            HashMap<Character, Integer> map = new HashMap<>();
            int start = -1, end = -1;
            int maxValue = 0, count = 0;
            while (true) {
                if (count <= m) {
                    ++end;
                    if (end == line.length())
                        break;
                    char key = line.charAt(end);
                    if (map.containsKey(key)) {
                        map.put(key, map.get(key) + 1);
                        if (map.get(key) == 1)
                            ++count;
                    } else {
                        map.put(key, 1);
                        ++count;
                    }
                    if (count <= m && maxValue < end - start)
                        maxValue = end - start;

                } else {
                    ++start;
                    char key = line.charAt(start);
                    map.put(key, map.get(key) - 1);
                    if (map.get(key) == 0)
                        --count;
                }
            }

            builder.append(maxValue + "\n");
        }

        System.out.print(builder);
    }
}
