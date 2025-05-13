import re

# Assembly code as per question (C)2
code = [
    "START 300",
    "READ M",
    "READ N",
    "MOVER AREG, ='51'",
    "MOVER BREG, ='61'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, M",
    "ADD CREG, ='11'",
    "COMP CREG, N",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='11'",
    "COMP AREG, N",
    "BC GT, NEXT",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

# Initialize literal table and location counter
literal_table = {}
loc_counter = 0

# First Pass: Collect all literals
for line in code:
    line = line.strip()
    if not line:
        continue

    parts = line.split()

    # Handle START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Find literals using regex
    literals = re.findall(r"='(\d+)'", line)
    for lit in literals:
        literal_token = f"='{lit}'"
        if literal_token not in literal_table:
            literal_table[literal_token] = None  # Address will be assigned later

    # Increment location counter (assume each instruction is 1 word)
    if parts[0] != "END":
        loc_counter += 1

# Second Pass: Assign memory addresses to literals
literal_address = loc_counter
for literal in literal_table:
    literal_table[literal] = literal_address
    literal_address += 1

# Print the Literal Table
print("Literal Table")
print("Literal\tAddress")
for literal, address in literal_table.items():
    print(f"{literal}\t{address}")
