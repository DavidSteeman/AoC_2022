package day17;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

public class Grid {

    private BigInteger cum_top = BigInteger.ZERO;
    private int top = 0;
    private int[][] field = new int[1000000][7];
    private int[] left_bound = {0,0};
    private int[] right_bound = {6,0};


    public int get_top() {
        return top;
    }

    public BigInteger get_cum_top() {
        // System.out.println(cum_top);
        // System.out.println(top);
        return cum_top.add(BigInteger.valueOf((long) top));
    }

    public boolean topfill() {
        if (top == 0) {
            return true;
        }
        for (int x = 2; x < 6; x++) {
            if (field[top-1][x] == 1) {return true;}
        }
        return false;
    }

    public boolean check_pattern() {
        for (int start_y=0; start_y<43001; start_y++) {
            for (int target_y = start_y+5300; target_y < 46901; target_y++) {
                boolean pattern_match = true;
                for (int y_mod = 0; y_mod < 5300; y_mod++) {
                    for (int x = 0; x < 7; x++) {
                        if (field[start_y+y_mod][x] != field[target_y+y_mod][x]) {
                            pattern_match = false;
                            y_mod=5300;}
                    }
                }
                if (pattern_match) {
                    System.out.println("YES! " + start_y + " : " + target_y); 
                    start_y += 5300;
                    target_y = 50000;
                    // return true;
                }
            }
        }
        return false;
    }


    private void trim_field() {
        int cutoff = get_cutoff();
        if (cutoff > 0) {
            int bot_y = cutoff;
            
            if (bot_y > 0) {
                cum_top = cum_top.add(BigInteger.valueOf((long) bot_y));
                int new_top = top - bot_y + 1;
                for (int y = 0; y < new_top; y++) {
                    for (int x = 0; x < 7; x++) {
                        field[y][x] = field[y+bot_y][x];
                    }
                }

                for (int y = new_top; y <= top; y++) {
                    for (int x = 0; x < 7; x++) {
                        field[y][x] = 0;
                    }
                }
                top = new_top - 1;
                // System.out.println("New bot: " + bot_y);
                // System.out.println("New top: " + top);
            }
        }
    }


    public int[][] init_piece(int[][] piece) {
        int[][] new_piece = new int[piece.length][2];
        for (int sq = 0; sq < piece.length; sq++) {
            int[] new_sq = {piece[sq][0], piece[sq][1] + top + 3};
            new_piece[sq] = new_sq;
        }
        return new_piece;
    }


    private boolean collide(int[] pos) {
        int x = pos[0];
        int y = pos[1];
        if (x < 0 || x > 6 || y < 0) {
            return true;
        } else {
            // System.out.println(x + " " + y);
            if (field[y][x] != 0) {
                return true;
            }
        }
        return false;
    }


    public int[][] move_piece(int[][] piece, int[] dir) {
        int[][] new_piece = new int[piece.length][2];
        for (int block = 0; block < piece.length; block++) {
            int[] new_block = {piece[block][0] + dir[0], piece[block][1] + dir[1]};
            if (collide(new_block)) {
                return piece;
            } else {
                new_piece[block] = new_block;
            }
        }
        return new_piece;
    }


    public void place_piece(int[][] piece) {
        int[] bound = null; 
        for (int sq = 0; sq < piece.length; sq++) {
            int x = piece[sq][0];
            int y = piece[sq][1];
            field[y][x] = 1;
            if (x == 0 || x == 6) {
                bound = new int[2];
                bound[0] = x;
                bound[1] = y;
            }
        }
        if (bound != null) {
            if (bound[0] == 0) {left_bound = bound;}
            else {right_bound = bound;}
        }
    }


    public void insert_piece(int[][] piece) {
        int[] bound = {0,0};
        for (int sq = 0; sq < piece.length; sq++) {
            int x = piece[sq][0];
            int y = piece[sq][1];
            field[y][x] = 1;
            if (y >= top) {top = y + 1;};
            if (x == 0) {
                bound[0] = y;
            } else if (x == 6) {
                bound[1] = y;
            }
        }
        if (bound[0] > 0) {
            left_bound[1] = bound[0];
            if (top > 999900) {trim_field();}
        } else if (bound[1] > 0) {
            right_bound[1] = bound[1];
            if (top > 999900) {trim_field();}
        }
    }


    public void remove_piece(int[][] piece) {
        for (int sq = 0; sq < piece.length; sq++) {
            int x = piece[sq][0];
            int y = piece[sq][1];
            field[y][x] = 0;
        }
    }


    public void print_field(int start_y, int end_y) {
        if (start_y < 0 || start_y > end_y || end_y < 0 || end_y > 999) {
            System.out.println("Illegal field y bounds given.");
        } else {
            for (int y = end_y; y >= start_y; y--) {
                System.out.println(Arrays.toString(field[y]));
            }
        }
    }

    private int manhattan_distance(int[] point_a, int[] point_b) {
        int x_diff = Math.abs(point_a[0] - point_b[0]);
        int y_diff = Math.abs(point_a[1] - point_b[1]);
        return x_diff + y_diff;
    }

    private String loc_to_string(int[] loc) {
        return loc[0] + ":" + loc[1];
    }

    private HashMap<String, int[]> find_path() {
        HashMap<String, int[]> came_from = new HashMap<>();
        HashMap<String, Integer> cost_so_far = new HashMap<>();
        PriorityQueue<int[]> frontier = new PriorityQueue<int[]>( 
            (a, b) -> manhattan_distance(a, right_bound) - manhattan_distance(b, right_bound));
        came_from.put(loc_to_string(left_bound), null);
        cost_so_far.put(loc_to_string(left_bound), 0);

        int[] next = left_bound; 
        int x, y = 0;
        int[][] dirs = {{-1,0}, {0,1}, {1,0}, {0,-1}};

        while (next[0] != right_bound[0] || next[1] != right_bound[1]) {
            for (int[] dir : dirs) {
                x = next[0] + dir[0];
                y = next[1] + dir[1];
                if (x >= 0 && x < 7  && y >= 0) {
                    if (field[y][x] == 1) {
                        int[] loc = {x, y};
                        String locstring = loc_to_string(loc);
                        int cost = cost_so_far.get(loc_to_string(next)) + 1;
                        if (cost_so_far.containsKey(locstring)) {
                            if (cost_so_far.get(locstring) > cost) {
                                cost_so_far.put(locstring, cost);
                                came_from.put(locstring, next);
                            }
                        } else {
                            came_from.put(locstring, next);
                            cost_so_far.put(locstring, cost);
                            frontier.add(loc);
                        }
                    }
                }
            }
            
            next = frontier.poll();
            if (next == null) {
                System.out.println("No link between right bound and left bound discovered");
                return null;
            }
        }
        return came_from;
    }

    private int get_cutoff() {
        HashMap<String, int[]> path = find_path();
        if (path == null) {
            return 0;
        }
        ArrayList<int[]> traceback = new ArrayList<>();
        traceback.add(right_bound);
        while (traceback.get(0) != left_bound) {
            int[] prev_step = path.get(loc_to_string(traceback.get(0)));
            traceback.add(0, prev_step);
        }
        int low_point = 999999999;
        for (int[] loc : traceback) {
            int tb_y = loc[1];
            if (tb_y < low_point) {
                low_point = tb_y;
            }
        }
        // System.out.println(low_point);
        return low_point;
    }
}