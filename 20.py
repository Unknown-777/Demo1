import re

def generate_mnt_and_mdt(code):
    mnt = []
    mdt = []
    lines = code.strip().splitlines()
    current_macro = None
    current_params = []
    mdt_index = 0
    macro_start_index = {}

    for line in lines:
        line = line.strip()

        # Detect start of macro
        macro_match = re.match(r"MACRO\s+(\w+)(\s+(.*))?", line)
        if macro_match:
            macro_name = macro_match.group(1)
            params_str = macro_match.group(3) if macro_match.group(3) else ""
            current_params = [p.strip() for p in params_str.split(",") if p.strip()]
            macro_start_index[macro_name] = mdt_index
            mnt.append((macro_name, len(current_params), mdt_index))
            current_macro = macro_name
            continue

        if current_macro:
            if line == "MEND":
                mdt.append(f"({mdt_index}) MEND")
                mdt_index += 1
                current_macro = None
                current_params = []
                continue

            # Replace parameters with #1, #2, ...
            line_parts = line.split()
            for i, part in enumerate(line_parts):
                if part in current_params:
                    line_parts[i] = f"#{current_params.index(part) + 1}"
            processed_line = " ".join(line_parts)
            mdt.append(f"({mdt_index}) {processed_line}")
            mdt_index += 1

    return mnt, mdt

# === Input Code ===
input_code = """
LOAD J
STORE M
MACRO EST1
LOAD e
ADD d
MEND
MACRO EST ABC
EST1
STORE ABC
MEND
MACRO ADD7 P4, P5, P6
LOAD P5
EST 8
SUB4 2
STORE P4
STORE P6
MEND
EST
ADD7 C4, C5, C6
END
"""

# Generate tables
mnt, mdt = generate_mnt_and_mdt(input_code)

# === Print Macro Name Table ===
print("Macro Name Table (MNT):")
print("Name of Macro | No. of Parameters | MDT Index")
for name, param_count, index in mnt:
    print(f"{name:<14} | {param_count:<17} | {index}")

# === Print Macro Definition Table ===
print("\nMacro Definition Table (MDT):")
for entry in mdt:
    print(entry)
