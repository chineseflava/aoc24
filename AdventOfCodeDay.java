import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public abstract class AdventOfCodeDay {
    protected Scanner scanner;
    
    public AdventOfCodeDay(String filename){
        try{
            scanner = new Scanner(new File(filename));
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        }
    }

    public abstract int part1(List<List<String>> data);
    public abstract int part2(List<List<String>> data);
    protected List<List<String>> readLines(){
        List<List<String>> lines = new ArrayList<>();
        while (scanner.hasNextLine()){
            String line = scanner.nextLine();
            String[] items = line.split("\\s+"); //Split with one or more whitespaces.
            lines.add(List.of(items));
        }
        return lines;
    }
}
