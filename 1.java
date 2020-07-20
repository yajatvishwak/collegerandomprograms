import java.util.Scanner;

/*
4
1020304017018019020
*50607014015016
**809012013
***10011


3
10203010011012
*4050809
**607
*/

class Que1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = n * (n + 1);
        int t = 1;
        String s = "";

        for (int i = n; i >= 1; --i) {
            for (int k1 = i; k1 < n; k1++) { // prints stars
                
                s += "*";
            }

            for (int j = 1; j <= i; ++j) { // prints first half
                // System.out.print(t++ + "0");
                s += t++ + "0";
            }
            k = k - i;
            int temp = k + 1;
            for (int j = 1; j <= i; ++j) { // prints second half
                // System.out.print(temp++ + "0");
                s += temp++ + "0";
            }
            s = s.substring(0, s.length() - 1); // removes 0 from the string
            // System.out.println();
            s += "\n";
        }
        System.out.println(s);
    }

}
