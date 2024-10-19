import java.io.*;


public class Main {
    private static boolean check(String word) {
        int[] visited = new int[26];
        int prev = -1;
        int index;

        for (char c: word.toCharArray()) {
            index = c - 'a';
            if (index == prev) continue;
            if (visited[index] == 1) return false;
            prev = index;
            visited[index] = 1;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(reader.readLine());
        int count = 0;
        String word;
        for (int i = 0; i < N; ++i) {
            word = reader.readLine();
            if (check(word)) ++count;
        }

        writer.write(count + "\n");

        reader.close();
        writer.flush();
        writer.close();
    }
}