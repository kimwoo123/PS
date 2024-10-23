import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int Q = Integer.parseInt(reader.readLine());
        HashMap<String, PriorityQueue> map = new HashMap<>();

        long total = 0, value;
        int query, count;
        PriorityQueue<Long> heap;
        String k;
        while (Q-- > 0) {
            tokenizer = new StringTokenizer(reader.readLine());
            query = Integer.parseInt(tokenizer.nextToken());
            k = tokenizer.nextToken();
            count = Integer.parseInt(tokenizer.nextToken());
            if (query == 1) {
                if (map.containsKey(k) == false)
                    map.put(k, new PriorityQueue<Long>(Collections.reverseOrder()));
                heap = map.get(k);
                while (count-- > 0) {
                    value = Integer.parseInt(tokenizer.nextToken());
                    heap.offer(value);
                }
            }
            else {
                if(map.containsKey(k) == true) {
                    heap = map.get(k);
                    while (count-- > 0 && heap.isEmpty() == false) {
                        total += heap.poll();
                    }
                }
            }
        }

        System.out.print(total);
    }
}