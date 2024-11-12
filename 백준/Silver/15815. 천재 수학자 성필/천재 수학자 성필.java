import java.io.*;
import java.util.*;


public class Main {
    static String expression;

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        expression = reader.readLine();
        Stack<Integer> stack = new Stack<>();
        Character c;
        Integer a, b;
        for (int i = 0; i < expression.length(); ++i) {
            c = expression.charAt(i);
            if (Character.isDigit(expression.charAt(i)) == true) {
                stack.add(c - '0');
            } else {
                a = stack.pop();
                b = stack.pop();
                if (c.equals('*') == true) {
                    stack.add(b * a);
                } else if (c.equals('+') == true) {
                    stack.add(b + a);
                } else if (c.equals('-') == true) {
                    stack.add(b - a);
                } else if (c.equals('/') == true) {
                    stack.add(b / a);
                }
            }
        }

        System.out.print(stack.pop());
    }
}
