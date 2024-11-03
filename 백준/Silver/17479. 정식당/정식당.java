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

        int N = Integer.parseInt(reader.readLine());
        HashMap<String, Long> countList = new HashMap<>();
        for (int i = 0; i < N; ++i) {
            name = reader.readLine();
            if (countList.containsKey(name))
                countList.put(name, countList.get(name) + 1);
            else
                countList.put(name, 1L);
        }

        Long value;
        Long total = 0L;
        Long sum = 0L;
        for (String key : countList.keySet()) {
            value = countList.get(key);
            if (normalList.contains(key)) {
                total += menuList.get(key) * value;
                sum += value;
            }
        }

        if (sum != N && total < 20000) {
            System.out.print("No");
            return;
        }

        for (String key : countList.keySet()) {
            value = countList.get(key);
            if (specialList.contains(key)) {
                total += menuList.get(key) * value;
                sum += value;
            }
        }

        if (sum != N && total < 50000) {
            System.out.print("No");
            return;
        }

        Integer count = 0;
        for (String key : countList.keySet()) {
            if (serviceList.contains(key)) {
                ++count;
            }
        }

        if (count > 1) {
            System.out.print("No");
            return;
        }
        System.out.print("Okay");
    }
}
