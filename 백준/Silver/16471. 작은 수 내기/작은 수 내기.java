import java.io.*;
import java.util.*;


public class Main {
    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(reader.readLine());

        StringTokenizer tokenizer1 = new StringTokenizer(reader.readLine());
        StringTokenizer tokenizer2 = new StringTokenizer(reader.readLine());
        int[] list1 = new int[N];
        int[] list2 = new int[N];
        for(int i = 0; i < N; ++i) {
            list1[i] = Integer.parseInt(tokenizer1.nextToken());
            list2[i] = Integer.parseInt(tokenizer2.nextToken());
        }

        Arrays.sort(list1);
        Arrays.sort(list2);

        int k = 0;
        boolean flag;
        for (int i = 0; i < N/2 +1; ++i) {
            flag = false;
            for (int j = k; j < N; ++j) {
                if (list1[i] < list2[j]) {
                    k = j+1;
                    flag = true;
                    break;
                }
            }

            if (flag == false) {
                System.out.print("NO");
                return;
            }
        }

        System.out.print("YES");
    }
}
