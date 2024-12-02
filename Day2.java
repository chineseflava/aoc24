import java.util.List;

public class Day2 extends AdventOfCodeDay{
    public Day2(String filename){
        super(filename);
    }

    @Override
    public int part1(List<List<String>> data) {
        int score = 0;

        for(int i = 0; i < data.size() - 1; i++){
            if (safe_data(data.get(i))){
                score += 1;
            }
        }
        return score;
    }

    @Override
    public int part2(List<List<String>> data){
        int score = 0;
        return score;
    }

    public boolean safe_data(List<String> data){
        boolean safe = true;
        if (isSortedAsc(data) || isSortedDesc(data)){
            for (int i = 0; i < data.size() - 1; i++){
                int diff = Math.abs(Integer.valueOf(data.get(i))-Integer.valueOf(data.get(i+1)));
                if(diff > 3 || diff == 0){
                    safe = false;
                }
            }
        }else{
            safe = false;
        }
        return safe;
    }

    public static boolean isSortedAsc(List<String> list){
        for (int i = 0; i < list.size() -1; i++){
            if (Integer.valueOf(list.get(i)) > Integer.valueOf(list.get(i+1))){
                return false;
            }
        }
        return true;
    }

    public static boolean isSortedDesc(List<String> list){
        for (int i = 0; i<list.size() -1; i++){
            if (Integer.valueOf(list.get(i)) < Integer.valueOf(list.get(i+1))){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        String filename = "input/2";
        AdventOfCodeDay day2 = new Day2(filename);
        List<List<String>> data = day2.readLines();

        int answer1 = day2.part1(data);
        System.out.println("\nAnswer Part1: " + answer1);

        //int answer2 = day2.part2(data);
        //System.out.println("Answer Part2: " + answer2);
    }
}