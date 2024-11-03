import java.io.*;
import java.math.BigInteger;
import java.util.*;


public class Main {
    static int A, B, C;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        tokenizer = new StringTokenizer(reader.readLine());
        A = Integer.parseInt(tokenizer.nextToken());
        B = Integer.parseInt(tokenizer.nextToken());
        C = Integer.parseInt(tokenizer.nextToken());

        HashMap<String, Integer> menuList = new HashMap<>();
        String name;
        Integer cost;

        HashSet<String> normalList = new HashSet<>();
        for (int i = 0; i < A; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            name = tokenizer.nextToken();
            cost = Integer.parseInt(tokenizer.nextToken());
            menuList.put(name, cost);
            normalList.add(name);
        }

        HashSet<String> specialList = new HashSet<>();
        for (int i = 0; i < B; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            name = tokenizer.nextToken();
            cost = Integer.parseInt(tokenizer.nextToken());
            menuList.put(name, cost);
            specialList.add(name);
        }

        HashSet<String> serviceList = new HashSet<>();
        for (int i = 0; i < C; ++i) {
            name = reader.readLine();
            menuList.put(name, 0);
            serviceList.add(name);
        }

        long normalTotal = 0L;
        long specialTotal = 0L;
        long count = 0L;

        int N = Integer.parseInt(reader.readLine());
        HashMap<String, Long> countList = new HashMap<>();
        for (int i = 0; i < N; ++i) {
            name = reader.readLine();
            if (normalList.contains(name))
                normalTotal += menuList.get(name);
            else if (specialList.contains(name))
                specialTotal += menuList.get(name);
            else
                ++count;
        }

        if (normalTotal < 20000 && specialTotal > 0) {
            System.out.print("No");
        } else if (normalTotal + specialTotal < 50000 && count > 0){
            System.out.print("No");
        } else if (count > 1) {
            System.out.print("No");
        } else {
            System.out.print("Okay");
        }
    }
}
