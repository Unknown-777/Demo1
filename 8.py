import re

# Input code from the question
code = [
    "START 200",
    "READ X",
    "MOVER AREG, ='10'",
    "MOVEM AREG, Y",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "COMP AREG, X",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='10'",
    "MOVER CREG, Y",
    "ADD CREG, ='80'",
    "MOVEM CREG, Y",
    "PRINT B",
    "LAST STOP",
    "X DS 1",
    "Y DS 1",
    "END"
]

# Track literals, pool table, and their addresses
literal_table = []
pool_table = [0]  # First pool always starts at index 0
literal_address_map = {}
loc_counter = 200  # Starting location counter as per 'START 200'

# First pass: Extract literals and handle address allocation
for line in code:
    line = line.strip()
    if not line:
        continue

    parts = line.split()

    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Extract literals using regex
    literals = re.findall(r"='(\d+)'", line)
    for lit in literals:
        literal_token = f"='{lit}'"
        if literal_token not in literal_table:
            literal_table.append(literal_token)

    # Handle LTORG or END: Assign addresses to current pool literals
    if parts[0] in ["LTORG", "END"]:
        for lit in literal_table:
            if lit not in literal_address_map:
                literal_address_map[lit] = loc_counter
                loc_counter += 1
        if parts[0] == "LTORG":
            pool_table.append(len(literal_table))
    else:
        loc_counter += 1

# Print Literal Table
print("Literal Table")
print("Index\tLiteral\tAddress")
for idx, lit in enumerate(literal_table):
    print(f"{idx}\t{lit}\t{literal_address_map[lit]}")

# Print Pool Table
print("\nPool Table")
print("Pool#\tStart Index")
for idx, val in enumerate(pool_table):
    print(f"{idx + 1}\t{val}")
