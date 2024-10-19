import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] inputs = reader.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);

        HashSet<String> visited = new HashSet<>();
        for (int i = 0; i < N; ++i) {
           visited.add(reader.readLine());
        }

        ArrayList<String> result = new ArrayList<>();
        String str;
        for (int i = 0; i < M; ++i) {
            str = reader.readLine();
            if (visited.contains(str))
                result.add(str);
        }

        Collections.sort(result);
        writer.write(String.format("%d\n", result.size()));
        for (String s: result)
            writer.write(String.format("%s\n", s));

        reader.close();
        writer.flush();
        writer.close();
    }
}