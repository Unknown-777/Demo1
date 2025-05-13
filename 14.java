package prac;
import java.util.*;

public class prac1 {
    static List<String> source = Arrays.asList(
         "STORE P",
        "LOAD Q",
        "MACRO PCG",
        "LOAD m",
        "ADD n",
        "MEND",
        "LOAD H",
        "LOAD K",
        "MACRO ADDi PAR",
        "LOAD A",
        "STORE PAR",
        "MEND",
        "DIV R",
        "MACRO ADDii V1, V2, V3",
        "STORE V2",
        "ADDi  12",
        "ADDi   7",
        "LOAD V1",
        "LOAD V3",
        "MEND",
        "PCG",
        "ADDii Q1, Q2, Q3",
        "ADDi w",
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