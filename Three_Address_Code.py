import ast

class ThreeAddressCodeGenerator(ast.NodeVisitor):
    def __init__(self):
        self.temp_count = 1
        self.code = []
    
    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp
    
    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        temp = self.new_temp()
        op = self.get_operator(node.op)
        self.code.append(f"{temp} = {left} {op} {right}")
        return temp
    
    def visit_Name(self, node):
        return node.id

    def visit_Num(self, node):
        return str(node.n)
    
    def visit_Constant(self, node):  # for Python 3.8+
        return str(node.value)
    
    def get_operator(self, op):
        if isinstance(op, ast.Add): return '+'
        if isinstance(op, ast.Sub): return '-'
        if isinstance(op, ast.Mult): return '*'
        if isinstance(op, ast.Div): return '/'
        raise Exception(f"Unsupported operator: {type(op)}")

    def generate(self, expr):
        tree = ast.parse(expr, mode='exec')
        assign = tree.body[0]
        if not isinstance(assign, ast.Assign):
            raise Exception("Only assignment expressions are allowed.")
        
        target = assign.targets[0].id
        value = self.visit(assign.value)
        self.code.append(f"{target} = {value}")
        return self.code

# Main function
def main():
    expr = input("Enter expression (e.g., w = u*u - u*v + v*v): ")
    tac_generator = ThreeAddressCodeGenerator()
    try:
        tac = tac_generator.generate(expr)
        print("\nThree Address Code:")
        for line in tac:
            print(line)
    except Exception as e:
        print(f"Error: {e}")

main()
