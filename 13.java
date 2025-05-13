package prac;
import java.util.*;

public class prac1 {
    static List<String> source = Arrays.asList(
        "LOAD A",
        "MACRO ABC",
        "LOAD p",
        "SUB q",
        "MEND",
        "STORE B",
        "MULT D",
        "MACRO ADD1 ARG",
        "LOAD X",
        "STORE ARG",
        "MEND",
        "LOAD B",
        "MACRO ADD5 A1,A2,A3",
        "STORE A2",
        "ADD1 5",
        "ADD1 10",
        "LOAD A1",
        "LOAD A3",
        "MEND",
        "ADD1 t",
        "ABC",
        "ADD5 D1,D2,D3",
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