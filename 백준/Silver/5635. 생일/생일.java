import java.io.*;
import java.util.*;

public class Main {
    static class Person implements Comparable<Person> {
        String name;
        int day;
        int month;
        int year;

        Person(String name, int day, int month, int year) {
            this.name = name;
            this.day = day;
            this.month = month;
            this.year = year;
        }

        @Override
        public int compareTo(Person p) {
            if (this.year == p.year) {
                if (this.month == p.month) {
                    return Integer.compare(this.day, p.day);
                }
                return Integer.compare(this.month, p.month);
            }
            return Integer.compare(this.year, p.year);
        }

        @Override
        public String toString() {
            return this.name;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;

        int T;
        T = Integer.parseInt(reader.readLine());

        String name;
        int day, month, year, sum;
        ArrayList<Person> list = new ArrayList<>();
        for (int i=0; i < T; ++i) {
            tokenizer = new StringTokenizer(reader.readLine());
            name = tokenizer.nextToken();
            day = Integer.parseInt(tokenizer.nextToken());
            month = Integer.parseInt(tokenizer.nextToken());
            year = Integer.parseInt(tokenizer.nextToken());

            list.add(new Person(name, day, month, year));
        }

        Collections.sort(list);
        System.out.println(list.get(T-1));
        System.out.println(list.get(0));
    }
}