# Sample code as a list of lines
code = [
    "START 180",
    "READ M",
    "READ N",
    "LOOP MOVER AREG, M",
    "MOVER BREG, N",
    "COMP BREG, ='200'",
    "BC GT, LOOP",
    "BACK SUB AREG, M",
    "COMP AREG, ='500'",
    "BC LT, BACK",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

# List of known opcodes
opcodes = ["START", "READ", "MOVER", "COMP", "BC", "SUB", "STOP", "DS", "END"]

# Function to check if a word is an opcode
def is_opcode(word):
    return word in opcodes

symbol_table = {}
loc_counter = 0

# First Pass
for line in code:
    parts = line.strip().split()
    if not parts:
        continue

    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Check for label (not opcode at start)
    if not is_opcode(parts[0]):
        label = parts[0]
        if label not in symbol_table:
            symbol_table[label] = loc_counter

    # If DS, reserve specified memory
    if "DS" in parts:
        loc_counter += int(parts[-1])
    elif parts[0] != "END":
        loc_counter += 1

# Output symbol table
print("Symbol Table")
print("Symbol\tAddress")
for symbol, address in symbol_table.items():
    print(f"{symbol} \t {address}")
