import java.io.*;


public class Main {
    private static boolean check(String word) {
        boolean[] visited = new boolean[26];
        int prev = -1;
        int index;

        for (char c: word.toCharArray()) {
            index = c - 'a';
            if (index == prev) continue;
            if (visited[index] == true) return false;
            prev = index;
            visited[index] = true;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(reader.readLine());
        int count = 0;
        String word;
        for (int i = 0; i < N; ++i) {
            word = reader.readLine();
            if (check(word)) ++count;
        }

        System.out.println(count);
    }
}