class lexer:
    def tokline(self, line):
        tokens = []
        for ch in line:
            if len(tokens) == 0:
                tokens.append(ch)
                continue
            elif ch in '+-*/(){}<>[];:=$\'"':
                tokens.append(ch)
            elif ch in ' \t\n':
                tokens.append('')
            elif ch.isdigit():
                if tokens[-1].isdigit():
                    tokens[-1] = tokens[-1] + ch
                else:
                    tokens.append(ch)
            else:
                if tokens[-1] not in '+-*/(){}<>[];:=$\'"0123456789':
                    tokens[-1] = tokens[-1] + ch
                else:
                    tokens.append(ch)
        return [item for item in tokens if item != ""]
    def tokprogram(self, program):
        out = []
        for line in program:
            out.append(self.tokline(line))
        return [item for sublist in out for item in sublist]
class Node:
    def __init__(self, children=None, val=None, typet=None):
        self.children = children if children is not None else []
        self.val = val
        self.type = typet

class parser:
    def __init__(self):
        self.head = Node(children=[], val=None, typet='ROOT')
        self.current = self.head
    def buildast(self, program):
        for i in range(len(program)):
            if program[i] == 'var':
                VarNode = Node(typet='VARA')
                name = Node(val=program[i+1], typet='VARN')
                val = None
                temp = []
                for i in range(i+2, len(program)):
                    if program[i] == ';':
                        break
                    elif program[i] == '$':
                        temp.append(Node(val=program[i+1], typet='VARF'))
                    elif program[i].isdigit():
                        temp.append(Node(val=program[i], typet='LIT'))
                    elif program[i] == '+':
                        a = Node(children=[], val='OP+', typet='ADD')
                        a.children.append(temp.pop())
                        a.children.append(temp.pop())
                        temp.append(a)
                VarNode.children.append(name)
                for i in temp:
                    VarNode.children.append(i)
                self.head.children.append(VarNode)
    def printast(self, node, ind=0):
        if not isinstance(node, Node):
            print(node)
            return
        print(" "*ind , node.type, '->', node.val)
        for nod in node.children:
            self.printast(nod, ind+1)

        
if __name__ == '__main__':
    lex = lexer()
    par = parser()
    program = []
    with open('program.ol', 'r') as f:
        for line in f:
            program.append(line)
    tokens = lex.tokprogram(program)
    par.buildast(tokens)
    par.printast(par.head)