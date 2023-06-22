import sys
# initialization
programfilepath = input("program file path: ")
activefunc = False
variablename = []
funcname = []
funcvariable = []
firstwords = ["VAR","RET","FUNC"]
commandwords = ["VAR","RET","FUNC","EQUAL","ADD","SUB","MULT","DIV"]
with open(programfilepath) as programfile:
    program = programfile.readlines()
#operation functions
def add(a,b,res):
    if a not in variablename or b not in variablename or res not in variablename:
        sys.exit("Error: variable undefined at line " + str(program.index(line)+1))
    print("lod r1 " + str(variablename.index(a)+1))
    print("lod r2 " + str(variablename.index(b)+1))
    print("add r3 r1 r2")
    print("str " + str(variablename.index(a)+1) + " r3")


# first loop
for line in program: 
    instr = line.split()
    # variable error checks and initialization
    if instr[0] == "VAR":
        if len(instr) != 3:
            sys.exit("Error: expected 3 arguments, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
        if instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word at line: " + str(program.index(line)+1))
        if instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name \"" + instr[1] + "\" already in use at line: " + str(program.index(line)+1))
        variablename.append(instr[1])
    # function error checks and initialization
    if instr[0] == "FUNC":
        if len(instr) != 3:
            sys.exit("Error: expected 2 arguments, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
        if instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word at line: " + str(program.index(line)+1))
        if instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name \"" + instr[1] + "\" already in use at line: " + str(program.index(line)+1))
        if instr[2] in funcname or instr[2] in variablename:
            sys.exit("Error: name \"" + instr[2] + "\" already in use at line: " + str(program.index(line)+1))
        if activefunc == True:
            sys.exit("Error: cannot define a function within a function at line: " + str(program.index(line)+1))
        activefunc = True
        funcname.append(instr[1])    
        funcvariable.append(instr[2])
    # return error checks and initialization
    if instr[0] == "RET":
        if len(instr) >= 3:
            sys.exit("Error: expected 0-1 arguments, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
    if instr[0] == "END":
        if len(instr) != 1:
            sys.exit("Error: unexspected token at line" + str(program.index(line)+1))
        activefunc = False
# second loop
for line in program: 
    instr = line.split()
    if instr[0] == "VAR":
        print("str "+ str(variablename.index(instr[1])+1) + " " + instr[2])
    if instr[0] in variablename:
        if len(instr) != 3 and len(instr) != 5:
            sys.exit("Error: unexspected token \"" + " ".join(instr) + "\" at line " + str(program.index(line)+1))
        if len(instr) >= 2:
            if instr[1] != "EQUAL":
                sys.exit("Error: unexspected token \"" + " ".join(instr) + "\" at line " + str(program.index(line)+1))
            if instr[1] == "EQUAL": 
                if len(instr) == 5 and instr[3] == "ADD":
                    add(instr[2],instr[4],instr[0])

                    

