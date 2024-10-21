import java.io.*;
import java.util.*;


public class Main {
    private static int bisectLeft(int[] job_list, int target) {
        int start, end, mid;
        start = 0;
        end = job_list.length;
        while (start < end) {
            mid = (start + end) / 2;
            if (job_list[mid] <= target) start = mid+1;
            else end = mid;
        }
        return end-1;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int n, m;
        tokenizer = new StringTokenizer(reader.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());

        int[] job_list = new int[n+1];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 1; i < n+1; ++i)
            job_list[i] = job_list[i-1] + Integer.parseInt(tokenizer.nextToken());

        int target;
        for (int i = 0; i < m; ++i) {
            target = Integer.parseInt(reader.readLine());
            System.out.println(bisectLeft(job_list, target));
        }
    }
}