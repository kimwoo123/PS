import java.io.*;
import java.util.*;


public class Main {
    static int N;

    static class Lecture implements Comparable<Lecture> {
        int index;
        int start;
        int end;
        int room;

        Lecture(int i[], int room) {
            this.index = i[0];
            this.start = i[1];
            this.end = i[2];
            this.room = room;
        }

        @Override
        public int compareTo(Lecture l) {
            return this.end - l.end;
        }

        @Override
        public String toString() {
            return index + " " + start + " " + end;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        StringBuilder builder;

        N = Integer.parseInt(reader.readLine());

        ArrayList<int[]> queue = new ArrayList<>();
        int index, start ,end;
        for (int i = 0; i < N; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            index = Integer.parseInt(tokenizer.nextToken());
            start = Integer.parseInt(tokenizer.nextToken());
            end = Integer.parseInt(tokenizer.nextToken());

            queue.add(new int[] {index, start, end});
        }

        Collections.sort(queue, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });

        PriorityQueue<Lecture> pq = new PriorityQueue<>();
        Lecture lecture;
        int count = 0;
        int result = 0;
        int room;
        int[] roomList = new int[N];
        for (int i = 0; i < N; ++i) {
            lecture = new Lecture(queue.get(i), count+1);
            if (pq.isEmpty() == false && pq.peek().end <= lecture.start) {
                roomList[pq.peek().index-1] = pq.peek().room;
                room = pq.poll().room;
                lecture.room = room;
                --count;
            }
            pq.offer(lecture);
            ++count;
            if (result < count)
                result = count;
        }

        while (pq.isEmpty() == false) {
            lecture = pq.poll();
            roomList[lecture.index-1] = lecture.room;
        }

        builder = new StringBuilder();
        builder.append(result);
        for (int i = 0; i < N; ++i) {
            builder.append("\n" + roomList[i]);
        }

        System.out.print(builder);
    }
}
