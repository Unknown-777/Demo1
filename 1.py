code = [
    "START 100",
    "READ A",
    "READ B",
    "LOOP MOVER AREG, A",
    "     MOVER BREG, B",
    "     COMP BREG, ='2'",
    "     BC GT, LOOP",
    "BACK SUB AREG, B",
    "     COMP AREG, ='5'",
    "     BC LT, BACK",
    "     STOP",
    "A    DS 1",
    "B    DS 1",
    "END"
]

# List of known opcodes
opcodes = ["START", "READ", "MOVER", "COMP", "BC", "SUB", "STOP", "DS", "END"]

# Function to check if a word is an opcode
def is_opcode(word):
    return word in opcodes

symbol_table = {}
loc_counter = 0

for line in code:
    parts = line.strip().split()

    if not parts:
        continue

    # Handle START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # If the first word is not an opcode, it's a label
    if not is_opcode(parts[0]):
        label = parts[0]
        if label not in symbol_table:
            symbol_table[label] = loc_counter
        parts = parts[1:]  # Remove label to process opcode

    # For DS (Define Storage), increase loc_counter by given size
    if parts[0] == "DS":
        size = int(parts[1])
        loc_counter += size
    elif parts[0] != "END":
        loc_counter += 1

# Display the symbol table
print("Symbol Table")
print("Symbol\tAddress")
for symbol, address in symbol_table.items():
    print(f"{symbol}\t{address}")
