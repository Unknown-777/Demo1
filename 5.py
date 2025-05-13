import re

# Assembly source code (as per image B2)
code = [
    "START 200",
    "READ X",
    "READ Y",
    "MOVER AREG, ='5'",
    "MOVER BREG, ='6'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, X",
    "ADD CREG, ='1'",
    "COMP CREG, Y",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='1'",
    "COMP AREG, Y",
    "BC GT, NEXT",
    "STOP",
    "X DS 1",
    "Y DS 1",
    "END"
]

# Initialize
literal_table = {}
loc_counter = 0

# First Pass: Collect literals
for line in code:
    line = line.strip()
    if not line:
        continue

    parts = line.split()

    # Handle START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Find literals like ='5' using regex
    literals = re.findall(r"='(\d+)'", line)
    for lit in literals:
        literal_token = f"='{lit}'"
        if literal_token not in literal_table:
            literal_table[literal_token] = None  # Address will be assigned later

    # Increment location counter (assume 1 word per instruction)
    if parts[0] != "END":
        loc_counter += 1

# Second Pass: Assign addresses to literals starting at final loc_counter
literal_address = loc_counter
for literal in literal_table:
    literal_table[literal] = literal_address
    literal_address += 1

# Output the Literal Table
print("Literal Table")
print("Literal\tAddress")
for literal, address in literal_table.items():
    print(f"{literal}\t{address}")
