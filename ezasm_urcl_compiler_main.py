import sys
programfilepath = input("program file path: ")
activefunc = False
variablename = []
funcname = []
funcvariable = []
firstwords = ["VAR","RET","FUNC"]
commandwords = ["VAR","RET","FUNC","EQUAL","ADD","SUB","MULT","DIV"]

with open(programfilepath) as programfile:
    program = programfile.readlines()

for line in program: 
    instr = line.split()
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
        if activefunc == True:
            sys.exit("Error: cannot define a function within a function at line: " + str(program.index(line)+1))
        activefunc = True
        funcname.append(instr[1])    
        funcvariable.append(instr[2])
    if instr[0] == "RET":
        if len(instr) >= 3:
            sys.exit("Error: expected 0-1 arguments, got: " + str(len(instr)-1) + " at line: " + str(program.index(line)+1))
        activefunc = False

print(variablename)
print(funcname)
print(funcvariable)