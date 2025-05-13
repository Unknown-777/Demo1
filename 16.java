package prac;
import java.util.*;

public class prac1 {
    static List<String> source = Arrays.asList(
         "LOAD J",
        "STORE M",
        "MACRO EST",
        "LOAD e",
        "ADD d",
        "MEND",
        "LOAD S",
        "MACRO SUB4 ABC",
        "LOAD U",
        "STORE ABC",
        "MEND",
        "LOAD P",
        "ADD V",
        "MACRO ADD7 P4, P5, P6",
        "LOAD P5",
        "SUB4 XYZ",
        "SUB 8",
        "SUB 2",
        "STORE P4",
        "STORE P6",
        "MEND",
        "EST",
        "ADD7 C4, C5, C6",
        "SUB4 z",
        "END"
    );

    static List<String> intermediateCode = new ArrayList<>();

    public static void main(String[] args) {
        boolean inMacro = false;

        for (String line : source) {
            line = line.trim();
            if (line.startsWith("MACRO")) {
                inMacro = true;
            } else if (line.equals("MEND")) {
                inMacro = false;
            } else if (!inMacro) {
                intermediateCode.add(line);
            }
        }

        System.out.println("Intermediate Code:");
        intermediateCode.forEach(System.out::println);
    }
}