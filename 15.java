package prac;
import java.util.*;

public class prac1 {
    static List<String> source = Arrays.asList(
        "LOAD F",
        "STORE E",
        "MACRO SRS",
        "LOAD s",
        "SUB t",
        "MEND",
        "STORE k",
        "MACRO ADD3 XYZ",
        "LOAD U",
        "STORE XYZ",
        "MEND",
        "Add m",
        "MACRO ADD1 Si, Sii, Siii",
        "LOAD Sii",
        "ADD3 1",
        "ADD3 11",
        "STORE Si",
        "STORE Siii",
        "MEND",
        "SRS",
        "ADD1 C1, C2, C3",
        "ADD3 q",
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