import java.io.*;
import java.util.*;


public class Main {
    static class Info {
        int[] counts;
        int totalScore;
        int count;

        Info() {
            this.counts = new int[10];
        }

        @Override
        public String toString() {
            return "Counts: " + Arrays.toString(counts) + ", TotalScore: " + totalScore + ", Count: " + count;
        }
    }

    static int K;
    static int M, N, P;
    static int p, m, t, j;
    static Info info;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder = new StringBuilder();

        K = Integer.parseInt(reader.readLine());
        for (int i = 0; i < K; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            M = Integer.parseInt(tokenizer.nextToken());
            N = Integer.parseInt(tokenizer.nextToken());
            P = Integer.parseInt(tokenizer.nextToken());

            HashMap<Integer, Info> map = new HashMap<>();
            while (N-- > 0) {
                tokenizer = new StringTokenizer(reader.readLine());
                p = Integer.parseInt(tokenizer.nextToken());
                m = tokenizer.nextToken().charAt(0) - 'A';
                t = Integer.parseInt(tokenizer.nextToken());
                j = Integer.parseInt(tokenizer.nextToken());

                if (map.containsKey(p) == false) {
                    map.put(p, new Info());
                }

                info = map.get(p);
                if (j == 0 && info.counts[m] != -1) {
                    info.counts[m] += 1;
                }
                else if(j == 1 && info.counts[m] != -1) {
                    info.totalScore += t + (info.counts[m] * 20);
                    info.count += 1;
                    info.counts[m] = -1;
                }
            }

            List<Integer> keySet = new ArrayList<>(map.keySet());

            keySet.sort(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    Info i1, i2;
                    i1 = map.get(o1);
                    i2 = map.get(o2);
                    if (i1.count == i2.count) {
                        return Integer.compare(i1.totalScore, i2.totalScore);
                    }
                    return Integer.compare(i2.count, i1.count);
                }
            });

            builder = new StringBuilder();
            builder.append("Data Set " + (i+1) + ":\n");
            for (Integer k : keySet) {
                info = map.get(k);
                builder.append(k + " " + info.count + " " + info.totalScore + "\n");
            }

            System.out.print(builder);
            if (i != K-1)
                System.out.println();
        }
    }
}