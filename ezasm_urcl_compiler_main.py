import sys 
# initialization
programfilepath = input("program file path: ")
activefunc = False
variablename = []
funcname = []
funcvariable = []
commandwords = ["VAR","RET","FUNC","EQUAL","ADD","SUB","MULT","DIV","WHILE"]
comparisons = ["=","!=",">=","<=",">","<"]
numbers = [1,2,3,4,5,6,7,8,9,0]

with open(programfilepath) as programfile:
    program = programfile.readlines()
#operation functions
def add(a,b,res):
    if a not in variablename or b not in variablename or res not in variablename:
        sys.exit("Error: variable undefined at line " + str(program.index(line)+1))
    print("lod r1 m" + str(variablename.index(a)+1))
    print("lod r2 m" + str(variablename.index(b)+1))
    print("add r3 r1 r2")
    print("str m" + str(variablename.index(a)+1) + " r3")

def sub(a,b,res):
    if a not in variablename or b not in variablename or res not in variablename:
        sys.exit("Error: variable undefined at line " + str(program.index(line)+1))
    print("lod r1 m" + str(variablename.index(a)+1))
    print("lod r2 m" + str(variablename.index(b)+1))
    print("sub r3 r1 r2")
    print("str m" + str(variablename.index(a)+1) + " r3")

def mult(a,b,res):
    if a not in variablename or b not in variablename or res not in variablename:
        sys.exit("Error: variable undefined at line " + str(program.index(line)+1))
    print("lod r1 m" + str(variablename.index(a)+1))
    print("lod r2 m" + str(variablename.index(b)+1))
    print("mlt r3 r1 r2")
    print("str m" + str(variablename.index(a)+1) + " r3")

def div(a,b,res):
    if a not in variablename or b not in variablename or res not in variablename:
        sys.exit("Error: variable undefined at line " + str(program.index(line)+1))
    print("lod r1 m" + str(variablename.index(a)+1))
    print("lod r2 m" + str(variablename.index(b)+1))
    print("div r3 r1 r2")
    print("str m" + str(variablename.index(a)+1) + " r3")

# first loop
for line in program: 
    instr = line.split()
    
    if instr[0] == "VAR":
        if len(instr) != 3:
            sys.exit("Error: expected 2 arguments, got: " + str(len(instr)-1) + " : at line: " + str(program.index(line)+1))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(program.index(line)+1))
        elif instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name \"" + instr[1] + "\" already in use: at line: " + str(program.index(line)+1))
        elif instr[1][0] in  numbers:
            sys.exit("Error: variable name cannot contain a number at the start: at line " + str(program.index(line)+1))
        variablename.append(instr[1])
    
    elif instr[0] == "FUNC":
        if len(instr) != 3:
            sys.exit("Error: expected 2 arguments, got: " + str(len(instr)-1) + " :at line: " + str(program.index(line)+1))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(program.index(line)+1))
        elif instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name \"" + instr[1] + "\" already in use: at line: " + str(program.index(line)+1))
        elif instr[2] in funcname or instr[2] in variablename:
            sys.exit("Error: name \"" + instr[2] + "\" already in use: at line: " + str(program.index(line)+1))
        elif activefunc == True:
            sys.exit("Error: cannot define a function within a function: at line: " + str(program.index(line)+1))
        activefunc = True
        funcname.append(instr[1])    
        funcvariable.append(instr[2])

    elif instr[0] == "RET":
        if len(instr) >= 3:
            sys.exit("Error: expected 0-1 arguments, got: " + str(len(instr)-1) + " : at line: " + str(program.index(line)+1))

    elif instr[0] == "END":
        if len(instr) != 1:
            sys.exit("Error: unexpected token: at line" + str(program.index(line)+1))
        activefunc = False
    
    elif instr[0] == "WHILE":
        if len(instr) != 4:
            sys.exit("Error: expected 3 arguments, got: " + str(len(instr)-1) + " : at line: " + str(program.index(line)+1))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(program.index(line)+1))
        elif instr[2] in commandwords:
            sys.exit("Error: name \"" + instr[2] + "\" cannot be a command word: at line: " + str(program.index(line)+1))
        elif instr[2] not in comparisons:
            sys.exit("Error: invalid comparison \"" + instr[2] + "\": at line" + str(program.index(line)+1))
        elif instr[3] in commandwords:
            sys.exit("Error: name \"" + instr[3] + "\" cannot be a command word: at line: " + str(program.index(line)+1))
                         
# second loop
for line in program: 
    instr = line.split()
    if instr[0] == "VAR":
        print("str m"+ str(variablename.index(instr[1])+1) + " " + instr[2])
    elif instr[0] in variablename:
        if len(instr) != 3 and len(instr) != 5:
            sys.exit("Error: unexpected token \"" + " ".join(instr) + "\" at line " + str(program.index(line)+1))
        if len(instr) >= 2:
            if instr[1] != "EQUAL":
                sys.exit("Error: unexpected token \"" + " ".join(instr) + "\" at line " + str(program.index(line)+1))
            elif instr[1] not in variablename and not instr[1].isnumeric():
                sys.exit("Error: unexpected argument \"" + instr[1] + "\": at line: " + str(program.index(line)+1))
            elif instr[3] not in variablename and not instr[3].isnumeric():
                sys.exit("Error: unexpected argument \"" + instr[3] + "\": at line: " + str(program.index(line)+1)) 
            elif len(instr) == 5 and instr[3] == "ADD":
                add(instr[2],instr[4],instr[0])
            elif len(instr) == 5 and instr[3] == "SUB":
                sub(instr[2],instr[4],instr[0])
            elif len(instr) == 5 and instr[3] == "MULT":
                mult(instr[2],instr[4],instr[0])
            elif len(instr) == 5 and instr[3] == "DIV":
                div(instr[2],instr[4],instr[0])