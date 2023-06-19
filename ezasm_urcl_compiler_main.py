import sys
programfilepath = input("program file path: ")
variablename = []
funcname = []
funcvariable = []
firstwords = ["VAR","RET",]
commandwords = ["VAR","RET","FUNC","EQUAL","ADD","SUB","MULT","DIV"]
with open(programfilepath) as programfile:
    program = programfile.readlines()
for line in program: 
    instr = line.split()
    if instr[1] in firstwords and len(instr) == 1:
        sys.exit("Error: expected 1 argument, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
    if instr[0] == "VAR":
        if len(instr) != 2:
            sys.exit("Error: expected 1 arguments, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
        if instr[1] in commandwords:
            sys.exit("Error: name canot be a command word at line: " + str(program.index(line)+1))
        if instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name already in use at line: " + str(program.index(line)+1))
        variablename.append(instr[1])
    if instr[0] == "FUNC":
        if len(instr) != 3:
            sys.exit("Error: expected 2 arguments, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
        if instr[1] in commandwords:
            sys.exit("Error: name canot be a command word at line: " + str(program.index(line)+1))
        if instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name already in use at line: " + str(program.index(line)+1))
        if instr[2] in funcname or instr[2] in variablename:
            sys.exit("Error: name already in use at line: " + str(program.index(line)+1))
        funcname.append(instr[1])    
        funcvariable.append(instr[2])
print(variablename)
print(funcname)
print(funcvariable)