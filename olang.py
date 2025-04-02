import sys

class stack:
    def __init__(self):
        self.arr = []
        self.pt = -1
    def push(self, element):
        print(self.arr)
        self.arr.append(element)
        self.pt += 1
    def pop(self):
        print(self.arr, '|')
        return self.arr.pop()
    def top(self):
        return self.arr[-1]

class lexer:
    def tokline(self, line):
        tokens = []
        i = 0
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
        return out
class interpreter:
    def __init__(self):
        self.varibles = {}
        self.functions = {}
    def runline(self, line):
        for i in range(len(line)):
            token = line[i]
            if token == '=':
                self.varibles[line[i-1]] = line[i+1]
            elif token == ';':
                break
            elif token == 'show':
                if line[i+1] == '$':
                    print(self.varibles[line[i+2]])
                    continue
                for j in range(i+2, len(line)):
                    string = []
                    if line[j] == '"':
                        break
                    string.append(line[j])
                    i = j
                    print(" ".join(string))
    def runprogram(self, program):
        for line in program:
            self.runline(line)
if __name__ == '__main__':
    s = stack()
    lex = lexer()
    inp = interpreter()
    program = []
    with open('program.ol') as f:
        for line in f:
            program.append(line)
    tokens = lex.tokprogram(program)
    inp.runprogram(tokens)