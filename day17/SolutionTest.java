package day17;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class SolutionTest {
    private static int[][][] PIECES =  {{{2,0}, {3,0}, {4,0}, {5,0}},
                                        {{2,1}, {3,0}, {3,1}, {3,2}, {4,1}},
                                        {{2,0}, {3,0}, {4,0}, {4,1}, {4,2}},
                                        {{2,0}, {2,1}, {2,2}, {2,3}},
                                        {{2,0}, {3,0}, {2,1}, {3,1}}};
    private static int[][] a = {{0,0,0,1}, {0,1,1,0}, {0,1,0,1}, {0,0,0,1}, 
                                {1,0,1,0}, {0,0,0,1}, {0,1,1,0}, {0,1,0,1}, {1,1,1,0}};

    private static boolean check_trirow(int pattern_y) {
        for (int target_y = pattern_y+3; target_y < 6; target_y++) {
            boolean pattern_match = true;
            for (int y_mod = 0; y_mod < 3; y_mod++) {
                for (int x = 0; x < 4; x++) {
                    if (a[pattern_y+y_mod][x] != a[target_y+y_mod][x]) {pattern_match = false;}
                }
            }
            if (pattern_match) {System.out.println("YES! " + target_y); return true;}
        }
        return false;
    }

    public static void main(String[] args) {
        BigInteger a = new BigInteger("1000000000000");
        BigInteger b = a.subtract(new BigInteger("14")).divide(new BigInteger("70"));
        BigInteger c = a.subtract(new BigInteger("14")).remainder(new BigInteger("70"));
        System.out.println(b.multiply(new BigInteger("70")));
        System.out.println(c);
        System.out.println(b.multiply(new BigInteger("106")).add(new BigInteger("203")));
        System.out.println(b.multiply(new BigInteger("106")).add(new BigInteger("79")));
        BigInteger d = a.subtract(new BigInteger("219")).divide(new BigInteger("1730"));
        BigInteger e = a.subtract(new BigInteger("219")).remainder(new BigInteger("1730"));
        System.out.println(d.multiply(new BigInteger("1730")));
        System.out.println(e);
        System.out.println(d.multiply(new BigInteger("2644")).add(BigInteger.valueOf((long) 2879)));
        System.out.println(d.multiply(new BigInteger("2644")).add(new BigInteger("2879")));
    }
}