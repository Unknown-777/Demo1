import re

# Assembly code input
code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, ='50'",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, A",
    "ADD CREG, ='10'",
    "COMP CREG, B",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='10'",
    "COMP AREG, B",
    "BC GT, NEXT",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

# Initialize literal table and location counter
literal_table = {}
loc_counter = 0

# -------------------
# PASS 1: Collect all literals
# -------------------
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
            literal_table[literal_token] = None  # Address to be assigned later

    # Increment location counter (1 per instruction)
    if parts[0] != "END":
        loc_counter += 1

# -------------------
# PASS 2: Assign addresses to literals
# -------------------
literal_address = loc_counter
for literal in literal_table:
    literal_table[literal] = literal_address
    literal_address += 1

# -------------------
# Output Literal Table
# -------------------
print("Literal Table")
print("Literal\tAddress")
for literal, address in literal_table.items():
    print(f"{literal}\t{address}")
