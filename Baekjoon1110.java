import java.util.*;
import java.io.*;
public class Baekjoon1110{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;
        int origin = N;
        do {
            N=((N%10)*10)+(((N/10)+(N%10))%10);
            count ++;
        } while (origin != N);

        System.out.println(count);
    }
}