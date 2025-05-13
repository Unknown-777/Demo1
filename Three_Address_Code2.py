import re

def generate_TAC(expression):
    tac_code = []
    # tokenize variables/operators/parentheses
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|[-+*/^=()]', expression)
    
    temp_counter = 1
    def new_temp():
        nonlocal temp_counter
        name = f"t{temp_counter}"
        temp_counter += 1
        return name

    # we'll convert infix → postfix (shunting-yard) to respect precedence, then eval postfix
    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    output_q = []
    op_stack = []

    for tok in tokens:
        if re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', tok):
            output_q.append(tok)
        elif tok in prec:
            while (op_stack and op_stack[-1] in prec and
                   ((prec[tok] <= prec[op_stack[-1]] and tok != '^') or
                    (prec[tok] < prec[op_stack[-1]] and tok == '^'))):
                output_q.append(op_stack.pop())
            op_stack.append(tok)
        elif tok == '(':
            op_stack.append(tok)
        elif tok == ')':
            while op_stack and op_stack[-1] != '(':
                output_q.append(op_stack.pop())
            op_stack.pop()  # pop '('
        elif tok == '=':
            # treat assignment as lowest-precedence operator
            while op_stack:
                output_q.append(op_stack.pop())
            op_stack.append(tok)

    while op_stack:
        output_q.append(op_stack.pop())

    # now evaluate postfix to TAC
    stack = []
    for tok in output_q:
        if re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]*', tok):
            stack.append(tok)
        elif tok in prec or tok == '=':
            if tok == '=':
                rhs = stack.pop()
                lhs = stack.pop()
                tac_code.append(f"{lhs} = {rhs}")
            else:
                r = stack.pop()
                l = stack.pop()
                t = new_temp()
                tac_code.append(f"{t} = {l} {tok} {r}")
                stack.append(t)

    return tac_code

if __name__ == "__main__":
    expr = input("Enter an expression (e.g. a = f ^ r - u * f * t - p): ").strip()
    print("\nGenerated Three-Address Code:")
    for line in generate_TAC(expr):
        print(line)
